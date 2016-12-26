"""
READING DATA FROM CERTAIN RANGES ONLY
READING DATA FROM MULTIPLE FILES AND AGGREGATE
BUILDING, JOINING DATAFRAMES
"""

import pandas as pd

def create_empty_dataframe_index_dates():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    return pd.DataFrame(index = dates)
    
def add_data(dataframe, symbol):
    df = pd.read_csv("../data/{}.csv".format(symbol), index_col="Date", 
                     parse_dates=True, usecols=['Date', 'Adj Close'], 
                     na_values=['nan'])
    df = df.rename(columns = {'Adj Close' : symbol})
#    return dataframe.join(df).dropna()
    return dataframe.join(df, how='inner')
    
def run_this():
    foo = create_empty_dataframe_index_dates()
#    foo = add_data(foo, "../data/SPY.csv")
    for sym in ['AAPL', 'IBM', 'SPY']:
        foo = add_data(foo, sym)
        
    print foo
    
    

"""
Scope checking before running
"""
if __name__ == "__main__":
    run_this()