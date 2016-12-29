"""
Module containing utilities.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

def fill_missing_values(df_data):
    """Fill missing values in data frame, in place."""
    df_data.fillna(method="ffill", inplace="TRUE")
    return df_data.fillna(method="backfill", inplace="TRUE")


def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df_final = pd.DataFrame(index=dates)
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")

    for symbol in symbols:
        file_path = symbol_to_path(symbol)
        df_temp = pd.read_csv(file_path, parse_dates=True, index_col="Date",
            usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df_final = df_final.join(df_temp)
        if symbol == "SPY":  # drop dates SPY did not trade
            df_final = df_final.dropna(subset=["SPY"])
    return df_final.dropna()

def plot_data(df_data, title, ylabel):
    """Plot stock data with appropriate axis labels."""
    ax = df_data.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)
    plt.show()

def compute_daily_returns(df):
    dr = df.copy()
    dr[1:] = (df[1:] / df[:-1].values) - 1
    # dr.ix[0] = 0
    dr = dr[1:]
    return dr

def get_cumulative_returns(df):
    return (df[-1] / df[0]) - 1