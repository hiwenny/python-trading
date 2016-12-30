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

def get_rolling_mean(dataframe, nwindow=20):
    return pd.rolling_mean(dataframe, window=nwindow)

def get_rolling_std(dataframe, nwindow=20):
    return pd.rolling_std(dataframe, window=nwindow)

def get_bollinger_bands(rollingmean, rollingstd):
    return [rollingmean + 2*rollingstd, rollingmean - 2*rollingstd]

# used to compare between different stocks
def get_daily_returns(data):
    dr = data.copy()
    dr[1:] = (dr[1:] / dr[:-1].values - 1) # .values to force -1 shift of array, otherwise will default to per-element matching operation
    #then we sub the beginning and the end with 0s
    dr.ix[0, :] = 0
    return dr

def get_cumulative_returns(data):
    return (data[-1] / data[0]) - 1

def run_this():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = 'SPY'
    df = get_data(symbols, dates)

    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    rm_SPY = get_rolling_mean(df['SPY'], 20)
    rm_SPY.plot(label='Rolling mean', ax=ax)

    std_SPY = get_rolling_std(df['SPY'], 20)

    [upper_band, lower_band] = get_bollinger_bands(rm_SPY, std_SPY)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

    bx = df['SPY'].plot(title="SPY daily returns", label='SPY')
    daily_SPY = get_daily_returns(df)
    daily_SPY.plot(label='Daily returns', ax=bx)
    bx.set_xlabel("Date")
    bx.set_ylabel("Price")
    plt.show()
    cumulative_returns = get_cumulative_returns(df['SPY'])
    print(cumulative_returns)


if __name__ == "__main__":
    run_this()