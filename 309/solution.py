from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell1, sell2 = -prices[0], 0, 0
        for i in range(1, n):
            n_buy = max(buy, sell1 - prices[i])
            n_sell1 = max(sell1, sell2)
            n_sell2 = prices[i] + buy
            buy, sell1, sell2 = n_buy, n_sell1, n_sell2
        return max(sell1, sell2)
