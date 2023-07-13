import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[sys.maxsize] * (n + 2) for _ in range(n)]
        for i in range(1, n + 1):
            dp[0][i] = matrix[0][i - 1]
        for i in range(1, n):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i][j - 1] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
        return min(dp[n - 1][1:n + 1])
