'''
Two types of statistics:
    global, as computed from the total of all
    rolling, computed per-interval and moves alongside chart.

    BB is an application of rolling stddev +- 2*stddev, as a visual indicator
    of price deviation from setting the rolling average as the underlying price of stock.
'''
import matplotlib.pyplot as plt
import pandas as pd

def get_data(symbol, dates):
    df = pd.DataFrame(index=dates)
    rf = pd.read_csv("../data/{}.csv".format(symbol), index_col="Date",
                     parse_dates=True, usecols=['Date', 'Adj Close'],
                     na_values=['nan'])
    rf = rf.rename(columns={'Adj Close': symbol})
    return df.join(rf, how='inner')


def run_this():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = 'SPY'
    df = get_data(symbols, dates)

    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    rm_SPY = pd.rolling_mean(df['SPY'], window=20)
    rm_SPY.plot(label='Rolling mean', ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    run_this()