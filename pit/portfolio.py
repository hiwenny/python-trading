"""
Portfolio class containing methods and attributes.
Based on assignment as described in 0107_portfolio_assnment

The idea is to only need to feed in a raw dataframe and get processed portfolio dataframe out,
along with other calc methods associated.
"""
import pandas as pd
from util import get_data

class Portfolio(object):
    def __init__(self, raw_dataframe, starting_capital, allocation):
        self.raw_dataframe = raw_dataframe
        self.allocation = allocation
        self.starting_capital = starting_capital
        self.portfolio_dataframe = self.get_portfolio()
        self.portfolio_dataframe_daily = self.get_portfolio_daily()

    def get_portfolio(self):
        normed = self.raw_dataframe / self.raw_dataframe.ix[0]
        allocated = normed * self.allocation
        position_values = allocated * self.starting_capital
        return position_values

    def get_portfolio_values(self):
        return self.portfolio_dataframe.sum(axis=1)

    def get_cumulative_return(self):
        portfolio_values = self.portfolio_dataframe.sum(axis=1)
        return portfolio_values[-1] / portfolio_values[0] - 1

    def get_portfolio_daily(self):
        dr = self.portfolio_dataframe.copy()
        dr[1:] = (df[1:] / df[:-1].values) - 1
        return dr[1:]

    def get_average_daily_return(self):
        return self.portfolio_dataframe_daily.mean()

    def get_stddev_return(self):
        return self.portfolio_dataframe_daily.std()

    def get_sharpe_ratio(self, expected_risk_free_rate=0, expected_rfr_stddev=0, rfr_period='year', sampling_freq='day'):
        # measures risk-adjusted return
        # note that the timeframe of measurements and interest accrues of rfr must be the same.
        # here is DAILY
        if (rfr_period == 'year'):
            expected_risk_free_rate = (1 + expected_risk_free_rate) ** (1/252) - 1
        elif (rfr_period == 'month'):
            expected_risk_free_rate = (1 + expected_risk_free_rate) ** (1/21) - 1

        rate_of_return_expected = (self.portfolio_dataframe_daily - expected_risk_free_rate).mean()
        rate_of_return_stddev = (self.portfolio_dataframe_daily - expected_rfr_stddev).std()
        sharpe_per_measure = rate_of_return_expected / rate_of_return_stddev

        if (sampling_freq == 'year'):
            K = 1
        elif (sampling_freq == 'month'):
            K = 12 ** (1/2)
        elif (sampling_freq == 'week'):
            K = 52 ** (1/2)
        elif (sampling_freq == 'day'):
            K = 252 ** (1/2)

        sharpe_annual = sharpe_per_measure * K

        return sharpe_annual

if __name__ == "__main__":
    dates = pd.date_range('2009-01-01', '2012-12-31')
    df = get_data(['SPY', 'XOM', 'AAPL', 'GOOG'], dates)

    a = Portfolio(df, 100000, [0.25, 0.25, 0.25, 0.25])
    print(a.get_sharpe_ratio(expected_risk_free_rate=0.02))



    """
    # so this is not private

    a.starting_capital = 200000
    print (a.starting_capital)

    # how to privatise?
    # add dunder e.g. __attr
    # but gen.ly not needed - no get and set here
    """
