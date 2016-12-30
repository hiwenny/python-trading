# import pandas as pd
# from util import get_data

class Valuation(object):
    def __init__(self, current_price, assets_amount, liabilities_amount, shares_amount, intangibles_amount=0, discount_rate=0.0001, interest_rate=0):
        self.price = current_price
        self.assets = assets_amount
        self.liabilities = liabilities_amount
        self.intangibles_amount = intangibles_amount
        self.shares_amount = shares_amount
        self.discount_rate = discount_rate
        self.interest_rate = interest_rate

    def get_intrinsic_value(self):
        return self.price / self.discount_rate

    def get_book_value(self):
        return self.assets - self.liabilities

    def get_market_value(self):
        return self.price * self.shares_amount

    def add_asset(self, asset):
        return self.assets + asset

    def add_liability(self, liability):
        return self.liabilities + liability

if __name__ == "__main__":
    # dates = pd.date_range('2009-01-01', '2012-12-31')
    # df = get_data(['SPY', 'XOM', 'AAPL', 'GOOG'], dates)

    a = Valuation(10, 10, 10, 50000)
    print(a.assets)
    print(a.get_intrinsic_value())
    print(a.assets)