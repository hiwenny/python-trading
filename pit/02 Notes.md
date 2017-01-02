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
sum |stock| = 1.0
The | | is to neutralize the positions. + for long, - for short.
Maximising port, then, involves calc. for the optimum amount of shares % in port.

Return = Beta * MktMov-RFR + Alpha
ri(t) = B * rm(t)-rf(t) + L
Beta is modifier: how reactive the stock is to market movement.
    for a stock with Beta = 2, movement is 2 x market.
Alpha is the other factor. This is calculated from information and is somehow a certainty, a number
    while market movement is large uncertainty.
This method of valuation is different, almost opposite of value investing. But this is in line with
    the application: short term, fundamental, calculations - while value investing is more long-term, more uncertainties
    at least from the POV of calculable components.
Seems to be taking advantage of inefficiencies in the mkt? The time it takes for market value to adjust to true in-value.

APT
Extension of CAPM for the overall stock.
expected return = r(f) + W1 (b(1) x rp(1)) + W2 (b(2) x rp(2)) + ... + Wn (b(n) x rp(n))
Assuming we're very, very confident we can predict alpha, then it's a matter of zero-sum the market-based risk so return = RFR + alpha.
Alpha, then, is a measure of how well we've beaten the mkt (of be beaten, in that case).
Also remember that sum(W) = 1.0

02-06
Popular indicators:
    - Momentum = price[t] / price[t-n] - 1 where n = days. Ranges from -0.5 to +0.5
    - SMA = price[t] / price[t-n:t].mean() - 1. Range -0.5 to +0.5
        combine with momentum so at crossing - might be that momentum is strong enough to continue trend. Too far, and it might snap back - see BB below.
    - BB = (price[t] - SMA[t]) / (2 * std[t]). Range -1.0 to +1.0
        basically stddev x 2 limit on upper and bottom. Cross and it's too far gone, expected to snap back to SMA.
Note that it doesn't always snap back! If momentum is too strong, you is screwed. Also momentum can come out of the blue, not always in the opp. dir first.
Look for confirmation
Wait for conditions to be met
Not trading is always an option!

Normalize these. Actually, normalize every factor introduced into calc always.
(dock to -1 to +1)