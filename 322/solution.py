import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin > amount:
                continue
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != sys.maxsize else -1
