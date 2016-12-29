"""
Daily portfolio value
1. start with raw prices data (compiled into a table from what stocks you have in portfolio)
2. normalize. p / p[0]
3. multiply by % of that stock in your pf (alloc)
4. calculate position value, pos_vals, by alloced * start_val
5. calculate total portfolio as sum of pos_vals.

POSTPROCESSING
daily returns, exclude 0 at the start!!!!
daily_rets = daily_rets[1:]

WHAT TO DO WITH THE PRODUCED PORTFOLIO VALUE

SHARPE RATIO
a measure of risk adjusted ratio
- lower risk better
- higher return better
- also considers risk free RoR
Expected (Rp - Rf ) / stddev (Rp - Rf)
an ex ante measure, meaning forward looking since using expected

using rough measure of Rf = 0%, the formula is
mean daily_rets / stddev daily_rets

SR varies according to frequency of sampling. Original intent is annual, if else adjust
SR annual = K * SR
K = sqrt(samples per year)
so if measured weekly, equivalent SR annual = sqrt(52) * SRweekly

MAIN 4 THINGS FOR PORTFOLIO ASSESSMENT
1. Cumulative return
2. Avg daily return
3. Risk (stddev)
4. Sharpe ratio
Now build it!

PART 2: PORTFOLIO OPTIMIZATION
Combining the first part of the assignment with the optimization.
Do it!

"""
import matplotlib.pyplot as plt
import pandas as pd
from util import get_data, compute_daily_returns, get_cumulative_returns

def generate_portfolio(dataframe, start_value):
    normed = dataframe / dataframe.ix[0]
    allocs = [0.3, 0.4, 0.1, 0.2]
    alloced = normed * allocs
    position_values = alloced * start_value
    portfolio_values = position_values.sum(axis=1)
    return portfolio_values

def generate_portfolio_stats(portfolio_df):
    daily_portfolio_returns = compute_daily_returns(portfolio_df)
    cumulative_portfolio_returns = get_cumulative_returns(portfolio_df)
    return [daily_portfolio_returns, cumulative_portfolio_returns]
    # is there a better way to do this?

if __name__ == "__main__":
    dates = pd.date_range('2009-01-01', '2012-12-31')
    df = get_data(['SPY', 'XOM', 'AAPL', 'GOOG'], dates)
    pf_value = generate_portfolio(df, 100000)
