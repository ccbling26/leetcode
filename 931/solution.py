import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [sys.maxsize] * (n + 2)
        for i in range(n):
            dp[i + 1] = matrix[0][i]
        for i in range(1, n):
            pre = dp[1]
            for j in range(n):
                tmp = dp[j + 1]
                dp[j + 1] = matrix[i][j] + min(pre, dp[j + 1], dp[j + 2])
                pre = tmp
        return min(dp)
