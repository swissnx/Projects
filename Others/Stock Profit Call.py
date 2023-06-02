
class StockTrader:
    def __init__(self):
        self.__prices = []

    def __max_profit(self):
        if not self.__prices:
            return 0
        min_price = self.__prices[0]
        max_profit = 0
        for price in self.__prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

    def __run(self):
        self.set_prices_from_input()
        profit = self.__max_profit()
        print(f"The maximum profit that can be achieved is: {profit}")

    def run(self):
        try:
            self.__run()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def set_prices(self, prices):
        self.__prices = prices

    def set_prices_from_input(self):
        prices = input("Enter the stock prices separated by spaces: ")
        prices = [int(price) for price in prices.split()]
        self.set_prices(prices)


if __name__ == "__main__":
    trader = StockTrader()
    trader.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# The maximum profit is calculated by the __max_profit method of the StockTrader class. This method finds the maximum difference
# between any two stock prices in the list where the second price comes after the first price.
# In your example, the stock prices are [1, 5, 5, 2]. The maximum profit is achieved by buying the stock at a price of 1 and
# selling it at a price of 5, resulting in a profit of 5 - 1 = 4.