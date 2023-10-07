class StockSpanner:
    def __init__(self):
        self.p = []

    def next(self, price: int) -> int:
        q = (price, 1)
        while self.p and self.p[-1][0] <= price:
            q = (price, q[1] + self.p.pop()[1])
        self.p.append(q)
        return q[1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
