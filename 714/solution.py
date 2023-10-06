from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy, sell = -float('inf'), 0
        for i in range(n):
            buy, sell = max(buy, sell - prices[i]), max(sell, prices[i] + buy - fee)
        return sell
