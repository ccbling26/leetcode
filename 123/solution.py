from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1, buy2 = -prices[0], -prices[0]
        sell1, sell2 = 0, 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(prices[i] + buy1, sell1)
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(prices[i] + buy2, sell2)
        return sell2
