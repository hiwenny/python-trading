"""
Daily returns, on its own, are not very useful.
They are useful when compared to other stocks' returns, since it indicates if the phenomenon is
 across the market or exclusive to that particular stock and hence, its performance.
"""

import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data

def compute_daily_returns(df):
    dr = df.copy()
    dr[1:] = (df[1:] / df[:-1].values) - 1
    dr.ix[0, :] = 0
    return dr

def run_this():
    # Reading chart data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    # plot_data(df, title="Stock Data", ylabel="Price")

    # Computing daily returns
    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily Returns", ylabel="Daily returns")

    #Plotting hist
    daily_returns['SPY'].hist(bins=20, label='SPY')
    daily_returns['XOM'].hist(bins=20, label='XOM')
    plt.legend(loc='upper right')

    # Global
    # mean = daily_returns.mean()
    # std = daily_returns.std()
    # plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    # plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    # plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)

    plt.show()

    print (daily_returns.kurtosis())

run_this()