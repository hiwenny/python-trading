"""
Portfolio class containing methods and attributes.
Based on assignment as described in 0107_portfolio_assnment

The idea is to only need to feed in a raw dataframe and get processed portfolio dataframe out,
along with other calc methods associated.
"""
import matplotlib.pyplot as plt
import pandas as pd
from util import get_data, compute_daily_returns, get_cumulative_returns

class Portfolio(object):
    def __init__(self, raw_dataframe, starting_capital, allocation):
        self.raw_dataframe = raw_dataframe
        self.allocation = allocation
        self.starting_capital = starting_capital
        self.portfolio_dataframe = self.get_portfolio()
        self.portfolio_values = self.get_portfolio_values()

    def get_portfolio(self):
        normed = self.raw_dataframe / self.raw_dataframe.ix[0]
        allocated = normed * self.allocation
        position_values = allocated * self.starting_capital
        return position_values

    def get_portfolio_values(self):
        return self.portfolio_dataframe.sum(axis=1)

if __name__ == "__main__":
    dates = pd.date_range('2009-01-01', '2012-12-31')
    df = get_data(['SPY', 'XOM', 'AAPL', 'GOOG'], dates)

    a = Portfolio(df, 100000, [0.3, 0.4, 0.1, 0.2])
    print (a.portfolio_values)
