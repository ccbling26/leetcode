from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell1, sell2 = -prices[0], 0, 0
        for i in range(1, n):
            buy = max(buy, sell1 - prices[i])
            sell1 = sell2
            sell2 = max(sell2, prices[i] + buy)
        return max(sell1, sell2)
