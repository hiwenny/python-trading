"""
Three things:
- beta: angle between horz and linear-fit line, indicating reactiveness to market. Higher, more reactive.
- alpha: intersecting point between line and vertical axis, indicating performance of stock. Higher, better compared to mkt.
- correlation: the more points through, the more correlated its behavior. Not the angle!
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from util import get_data

def compute_daily_returns(df):
    dr = df.copy()
    dr[1:] = (df[1:] / df[:-1].values) - 1
    dr.ix[0, :] = 0
    return dr

def run_this():
    # Reading chart data
    plt.close('all')

    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    # plot_data(df, title="Stock Data", ylabel="Price")

    # Computing daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')
    print ("beta_XOM = ", beta_XOM)
    print ("alpha_XOM = ", alpha_XOM)

    #Scatterplot SPY vs GLD
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    plt.plot(daily_returns['SPY'], beta_GLD*daily_returns['SPY'] + alpha_GLD, '-', color='r')
    print ("beta_GLD = ", beta_GLD)
    print ("alpha_GLD = ", alpha_GLD)

    # BONUS: calculating corr coeff
    print (daily_returns.corr(method='pearson'))

    print (daily_returns.kurtosis())

    return plt.show()

run_this()