# v 0.2.0

# first, import the necessary modules
from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.by import By
import pandas as pd
import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import datetime
from shutil import copyfile
import yfinance

# first, select the csv file with the necessary information
root = Tk()
root.withdraw()
# source_data = askopenfilename()
# for now, just use the direct file path
stock_df = pd.read_csv('test_data.csv', index_col=False)
stock_df = stock_df.sort_values('Symbol')
print(stock_df)    # only here for debugger breakpoint purposes at this moment

# next, create a copy of the target_workbook.xslx document
# I will need to update the target workbook file; at this moment, it is missing several columns that I would like to include
target_workbook = f'target_workbook_{str(datetime.datetime.now())}.xlsx'
copyfile('target_workbook.xlsx', target_workbook)

# 