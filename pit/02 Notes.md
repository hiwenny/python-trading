Essentially a todo for the next steps.
Accompaniment to part 2 of course.


So. The portfolio calculation is done, then next step would be to build
PORTFOLIO OPTIMIZER
Performance: cumulative return, volatility, risk-adjusted return (Sharpe)
Minimzer to optimize portfolio
Problem: what is the optimum weighting of shares for max return?
Cumulative return: past performance to indicate future. Easiest, least dependable.
Minimizer:
1. profide a function to minimize f(x):
    biggest sharpe ratio:
    f(x) = -sharpe ratio
    # of dimensions equal to types of stocks in port
2. provide initial guess X
3. let it rip (till minima)

Ranges and constraints
- Ranges: limits on values
    x = 0:1 since 0%:100%
- Constraints: properties of X that must be true
    sum( |Xi| = 1.0 )

================================

02-03: The idea is to compare.

What affects stocks?
1. Market condition. Is the whole universe bad, or is it just Alderaan?
2. Sector condition. Is it the whole Alderaan, or is it just the rainforest?
3. Individual company condition. Is it internal or external?

Valuation is 3 ways: book value, intrinsic value,market capitalization.
Mkt cap is what is there. The market reached an equilibrium, so what you see is the consensus at that time.
    Calculation is stock price * # of stocks
Book value is fact-based on the tangibles. Worst to worst, you can always sell it for scraps.
    Pretty reliable, careful of c(r)ooks.
Intrinsic value is expected payout over lifetime, using sum FV = PV / (1 - disc)^ to infinity, or 1 / disc for shorthand.
    This assumes payout so might be better for mature stocks.

General guide is mkt cap >= book value, since any lower and scrap value is higher = company no good.

================================

CAPM
Capital Asset Pricing Model
