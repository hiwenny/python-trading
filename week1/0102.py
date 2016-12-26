"""
READING DATA FROM CERTAIN RANGES ONLY
READING DATA FROM MULTIPLE FILES AND AGGREGATE
BUILDING, JOINING DATAFRAMES
PLOTTING MULTIPLE DATA
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def create_empty_dataframe_index_dates():
    start_date = '2010-01-22'
    end_date = '2010-02-26'
    dates = pd.date_range(start_date, end_date)
    return pd.DataFrame(index = dates)
    
def create_pathname(base, symbol):
    return os.path.join(base, "{}.csv".format(symbol))
    
def add_data(dataframe, base, symbol):
    pathname = create_pathname(base, symbol)
    df = pd.read_csv(pathname, index_col="Date", 
                     parse_dates=True, usecols=['Date', 'Adj Close'], 
                     na_values=['nan'])
    df = df.rename(columns = {'Adj Close' : symbol})
#    return dataframe.join(df).dropna()
    return dataframe.join(df, how='inner')
 
def plot_data(df, title="Stock prices"):
    '''Plot stock prices'''
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
    
def normalize_data(df):
    return df / df.ix[0, :]
    
def run_this():
    foo = create_empty_dataframe_index_dates()
    for sym in ['AAPL', 'IBM', 'SPY']:
        foo = add_data(foo, "../data", sym)
        
    # by row
    #print foo.ix['2010-01-01' : '2010-01-31']
    
    # by col
    #print foo['GOOG']
    #print foo[['IBM', 'GOOG']]
    
    # by row and col
    print foo.ix['2010-01-01':'2010-01-31', ['SPY', 'IBM']]
    plot_data(foo)

    # Normalization
    plot_data(normalize_data(foo))
    

"""
Scope checking before running
"""
if __name__ == "__main__":
    run_this()