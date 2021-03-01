# stock Class for the Fidelity Portfolio Review App
# at this point, I'm not sure if this is necessary

class Stock():

    def __init__(self, ticker):
        self.ticker = ticker
        self.account = None
        self.description = None
        self.quantity = None
        self.last_price = None
        self.last_price_change = None
        self.current_value = None
        self.todays_gain_loss_dollar = None
        self.todays_gain_loss_percent = None
        self.total_gain_loss_dollar = None
        self.total_gain_loss_percent = None
        self.percent_of_acct = None
        self.cost_basis = None
        self.cost_basis_per_share = None
        self.equity_summ_score = None
        self.recognia_short_term = None
        self.recognia_intermediate_term = None
        self.recognia_long_term = None
        self.valuation = None
        self.quality = None
        self.growth_stability = None
        self.financial_health = None
        self.pe_ttm = None
        self.pe_five_yr = None
        self.pcf_recent_quarter = None
        self.pcf_ttm = None
        self.ps_recent_quarter = None
        self.ps_ttm = None
        self.pb_ratio = None
