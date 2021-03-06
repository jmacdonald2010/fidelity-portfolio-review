from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import re

# I'm unsure if this will work or not, b/c I'm not sure if this file will be able to access the driver variable declared in the main notebook; going to use a driver parameter in the function that will be filled w/ the driver declared in the notebook

# used to determine the type of security being researched, as either a stock, ETF, or mutual fund
def determine_security_type(driver):
    try:
        sec_type = driver.find_element_by_class_name('breadcrumb-div')
    except:
        try:
            print('must be a MF')
            sec_type = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/header-template/div[1]/div[1]')
        except:
            print("Must not be a MF either, can't find anything")
            sec_type = 'Unknown'
            return sec_type
    try:
        sec_type = sec_type.text
        # print(sec_type)
    except AttributeError:
        pass
    sec_type.strip("»")
    sec_type = sec_type.split()
    for x in sec_type:
        if x == 'Stocks':
            sec_type = x
            return sec_type
        elif x == 'ETFs':
            sec_type = x
            return sec_type
        elif x == 'Mutual':
            sec_type = 'Mutual Funds'
            return sec_type

# Div yield for stocks
def stock_div_yield(driver):
    dividends = driver.find_elements_by_id('box11')
    dividends = dividends[0].text.split()
    for item in dividends:
        if '$' in item:
            div_amt = float(item.strip('$'))
        if '%' in item:
            div_yield = float(item.strip('%'))
    try:
        return div_amt, div_yield
    except:
        return 0, 0

# Equity Summary Score
def stock_equity_sum_score(driver):
    equity_summ_score = driver.find_element_by_class_name('rating-score')
    return float(equity_summ_score.text)

# Recognia Analysis
def recognia_analysis(driver, sec_type):
    if sec_type == 'Stocks':
        recognia_fixed_dict = {
            'Recognia Short Term': '/html/body/div[3]/div[2]/div[1]/div[11]/div/div/div/div/section/div/div[1]/div[2]',
            'Recognia Intermediate Term': '/html/body/div[3]/div[2]/div[1]/div[11]/div/div/div/div/section/div/div[2]',
            'Recognia Long Term': '/html/body/div[3]/div[2]/div[1]/div[11]/div/div/div/div/section/div/div[3]'
        }
    elif sec_type == 'ETFs':
        recognia_fixed_dict = {
            'Recognia Short Term': '/html/body/div[3]/div[2]/div[1]/div[7]/div/div/div/div/section/div/div[1]',
            'Recognia Intermediate Term': '/html/body/div[3]/div[2]/div[1]/div[7]/div/div/div/div/section/div/div[2]',
            'Recognia Long Term': '/html/body/div[3]/div[2]/div[1]/div[7]/div/div/div/div/section/div/div[3]'
        }

    recognia_dict = dict()

    for key, val in recognia_fixed_dict.items():
        element = driver.find_elements_by_xpath(val)
        elem_list = element[0].get_attribute('innerHTML').split()
        for i in range(0, len(elem_list)):
            if elem_list[i] == 'bold':
                result = elem_list[i + 1]
                result = re.findall(r'[a-z]*', result)
                recognia_dict[key] = result[0]
                break
    return recognia_dict

# Analysis: Valuation (Stocks)
def stock_valuation(driver):
    analysis_items = driver.find_element_by_class_name('analysis-items')
    valuation_pos = analysis_items.text.index('Valuation\ncurrent =')
    valuation = analysis_items.text[(valuation_pos + 19) : (valuation_pos + 23)]
    valuation = re.findall(r'\d+', valuation)
    return int(valuation[0])

# Analysis: Quality (Stocks)
def stock_quality(driver):
    analysis_items = driver.find_element_by_class_name('analysis-items')
    quality_pos = analysis_items.text.index("Quality")
    quality = analysis_items.text[(quality_pos + 18) : (quality_pos + 22)]
    quality = re.findall(r'\d+', quality)
    return int(quality[0])

# Analysis: Growth Stability (Stocks)
def stock_growth_stability(driver):
    analysis_items = driver.find_element_by_class_name('analysis-items')
    growth_stability_pos = analysis_items.text.index("Growth")
    growth_stability = analysis_items.text[(growth_stability_pos + 23) : (growth_stability_pos + 30)]
    growth_stability = re.findall(r"\d+", growth_stability)
    return int(growth_stability[0])

# Analysis: Financial Health (Stocks)
def stock_financial_health(driver):
    analysis_items = driver.find_element_by_class_name('analysis-items')
    fin_health_pos = analysis_items.text.index("Health")
    fin_health = analysis_items.text[(fin_health_pos + 15): (fin_health_pos + 20)]
    fin_health = re.findall(r"\d+", fin_health)
    return int(fin_health[0])

# 1-Yr Estimate (Stock)
def stock_one_yr_price_target(driver, symbol):
    driver.switch_to_window(driver.window_handles[1])
    driver.get(f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch')
    time.sleep(5)   # I don't think this will need automated scrolling down the page, not sure though.
    price_target = driver.find_elements_by_id('quote-summary')
    price_target = price_target[0].text.splitlines()
    # price_target
    for stat in price_target:
        if '1y Target' in stat:
            stat = stat.split()
            for x in stat:
                if '.' in x:
                    price_target = float(x)
                    break
    time.sleep(5)
    other_window = driver.window_handles[0] # switches back to the first open window (fidelity)
    # other_window
    driver.switch_to.window(window_name=other_window)
    if isinstance(price_target, float): 
        return price_target
    else:
        return np.nan

# key stats, including debt
# call this last, even though there are columns in the excel table after this
def stock_key_stats(driver, symbol):
    # first step is to navigate to the page w/ key stats on them
    driver.get(f'https://snapshot.fidelity.com/fidresearch/snapshot/landing.jhtml#/keyStatistics?symbol={symbol}')

    # then, we scroll thru the page like we did earlier to ensure all elements have rendered to the page and are thus accessible for us to extract

    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,(document.body.scrollHeight / 2))")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # next, we extract the information
    # a tuple containing all of the data we're looking for
    stats = ('P/E (Trailing Twelve Months)', 'P/E (5-Year Average)', 'Price/Cash Flow (Most Recent Quarter)', 'Price/Cash Flow (TTM)', 'Price/Sales (Most Recent Quarter)', 'Price/Sales (TTM)', 'Price/Book')

    stats_dict = dict()

    # extract data from the page
    key_stats = driver.find_elements_by_class_name('datatable-component')
    key_stats = key_stats[0].text.splitlines()

    for data in key_stats:
        for stat in stats:
            if stat in data:
                x = data.split()
                for y in x:
                    if '.' in y:
                        stats_dict[stat] = float(y.strip(','))
                        break
    
    # now, debt information extraction
    key_stats = driver.find_elements_by_class_name('datatable-component')
    key_stats = key_stats[4].text.splitlines()

    debt_stats = ('Total Debt/Equity (Most Recent Quarter, Annualized)', 'Total Debt/Equity (TTM)')
    debt_dict = dict()

    for stat in debt_stats:
        for x in key_stats:
            if stat in x:
                x = x.split()
                for text in x:
                    if '%' in text:
                        # text = text.strip(",")
                        text = re.sub('[\$,]', '', text)
                        debt_dict[stat] = float(text.strip(",").strip('%'))
                        break

    return stats_dict, debt_dict

# Extract 52 Week Performance for Stocks
def stock_52_week_perf(driver):
    fifty_two_week = driver.find_elements_by_id('box14')
    ftw_perf = fifty_two_week[0].text.splitlines()
    return float(ftw_perf[1].strip('+').strip('%'))

# ETF-Specific Functions

# ETF Key Stats
def etf_key_stats(driver):
    # I copied this straight from the sketches notebook, so I imagine it should work
    etf_stats = ('Price / Earnings (TTM)', 'Price / Book', 'Price / Sales', 'Price / Cash Flow', 'Distribution Yield')

    key_stats = driver.find_elements_by_id('keyStatistics-equity-data-table')
    try:
        key_stats = key_stats[0].text.splitlines()
    except IndexError:  # this may occur for fixed-income ETFs
        etf_stats_dict = {
            'Price / Earnings (TTM)': np.nan,
            'Price / Book': np.nan,
            'Price / Sales': np.nan,
            'Price / Cash Flow': np.nan,
            'Distribution Yield': np.nan,
        }
        return etf_stats_dict

    etf_stats_dict = dict()
    for x in range(len(key_stats)):
        for y in etf_stats:
            if y in key_stats[x]:
                if 'Distribution Yield' in key_stats[x]:
                    etf_stats_dict['etf_distribution_yield'] = float(key_stats[x + 2].strip('%').strip(','))
                else:
                    try:
                        etf_stats_dict[y] = float(key_stats[x + 1])
                    except ValueError:
                        etf_stats_dict[y] = np.nan

    return etf_stats_dict

# 52-Week Performance
def etf_52_week_perf(driver):
    ftwk_perf_etf = driver.find_elements_by_id('box14etf')
    ftwk_perf_etf = ftwk_perf_etf[0].text.splitlines()
    ftwk_perf_etf = ftwk_perf_etf[1].strip('+').strip('%')
    try:
        ftwk_perf_etf = float(ftwk_perf_etf)
    except ValueError:
        ftwk_perf_etf = np.nan
    return ftwk_perf_etf

# Mutual Fund-Specific Functions

# 52-Week Performance
def mf_52_week_perf(driver):
    mf_ftwk_perf = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div/div[1]/div[2]/performance-template/div/div[2]/div/div/div[2]/div[1]/p[2]')
    mf_ftwk_perf = float(mf_ftwk_perf[0].text.strip('+').strip('%'))
    return mf_ftwk_perf