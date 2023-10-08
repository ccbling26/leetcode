from heapq import heappop, heappush


class StockPrice:
    def __init__(self):
        self.prices = {}
        self.max_time = 0
        self.max_prices = []
        self.min_prices = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.max_time = max(self.max_time, timestamp)
        heappush(self.max_prices, (-price, timestamp))
        heappush(self.min_prices, (price, timestamp))

    def current(self) -> int:
        return self.prices[self.max_time]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.max_prices[0]
            if -price == self.prices[timestamp]:
                return -price
            heappop(self.max_prices)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.min_prices[0]
            if price == self.prices[timestamp]:
                return price
            heappop(self.min_prices)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
