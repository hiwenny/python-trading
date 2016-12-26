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
    
def add_data(dataframe, filepath):
    df = pd.read_csv(filepath)
    return dataframe.join(df)
    
def run_this():
    foo = create_empty_dataframe_index_dates()
    add_data(foo, "../data/AAPL.csv")
    print foo
    
run_this()