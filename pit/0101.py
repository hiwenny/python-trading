#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 07:34:04 2016

@author: wenny
"""

#"""
#READING DATA
#"""
#import pandas as pd
#def get_max_close(sym):
#    df = pd.read_csv("data/{}.csv".format(sym))
#    return df['Close'].max()
#        
#def get_mean(sym):
#    df = pd.read_csv("data/{}.csv".format(sym))
#    return df['Volume'].mean()
#
#def test_run():
#    for symbol in ['AAPL', 'IBM']:
#        print "Max close"
#        print symbol, get_max_close(symbol)
#        print "Mean volume"
#        print symbol, get_mean(symbol)
#        
#test_run()

# """
# PLOTTING DATA
# """
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph():
    df = pd.read_csv("../data/AAPL.csv")
    print df['High']
    df['High'].plot()
    plt.show() # the code above does not actually show the plot though it's there

# to plot two
def plot_two_graphs():
    df = pd.read_csv("../data/AAPL.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show() # the code above does not actually show the plot though it's there

plot_two_graphs()

"""
CSV IMPORTER BELOW
"""
# import pandas as pd
# import datetime
# from pandas_datareader import data
#
# tickers = ['AAPL', 'SPY' , 'IBM']
#
# for ticker in tickers:
#    end_date = datetime.datetime.now()
#    start_date = end_date - datetime.timedelta(days=365*10.0)
#    df = data.get_data_yahoo(ticker, start = start_date, end = end_date, interval='d')
#    df.to_csv("../data/{}.csv".format(ticker))