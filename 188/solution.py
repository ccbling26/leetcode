from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = [[float("-inf"), float("-inf")] for _ in range(k)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[0][0] = max(dp[0][0], -prices[i])
            dp[0][1] = max(dp[0][1], prices[i] + dp[0][0])
            for j in range(1, k):
                dp[j][0] = max(dp[j][0], dp[j - 1][1] - prices[i])
                dp[j][1] = max(dp[j][1], dp[j][0] + prices[i])
        return dp[k - 1][1]
