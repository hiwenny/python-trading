"""
Filling in missing data
Fill forward first
Then fill backwards
"""
import matplotlib.pyplot as plt
import pandas as pd

def get_data(symbol, dates):
    df = pd.DataFrame(index=dates)
    rf = pd.read_csv("../data/{}.csv".format(symbol), index_col="Date",
                     parse_dates=True, usecols=['Date', 'Adj Close'],
                     na_values=['nan'])
    rf = rf.rename(columns={'Adj Close': symbol})
    return df.join(rf, how='inner')

def plot(dataframe, title):
    ax = dataframe.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

def run_this():
    dates = pd.date_range('2005-12-31', '2014-12-07')
    symbols = 'FAKE2'
    df = get_data(symbols, dates)
    # the filling in part
    # fillna can work simult. for multiple data!
    df.fillna(method="ffill", inplace="TRUE")
    plot(df['FAKE2'], 'FAKE2')

if __name__ == "__main__":
    run_this()