from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            tmp = buy
            buy = max(buy, sell - prices[i])
            sell = max(sell, tmp + prices[i])
        return sell
