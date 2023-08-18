from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def calculate(slices):
            N, n = len(slices), (len(slices) + 1) // 3
            dp = [[-10**9 for i in range(n + 1)] for j in range(N)]
            dp[0][0], dp[0][1] = 0, slices[0]
            dp[1][0], dp[1][1] = 0, max(slices[0], slices[1])
            for i in range(2, N, 1):
                dp[i][0] = 0
                for j in range(1, n + 1, 1):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i])
            return dp[N - 1][n]
        v1 = slices[1:]
        v2 = slices[0:-1]
        ans1 = calculate(v1)
        ans2 = calculate(v2)
        return max(ans1, ans2)
