from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr.sort()
        n = len(arr)
        res, dp = 1, [1] * n
        for i in range(1, n):
            j, k = 0, i - 1
            while j <= k:
                val = arr[j] * arr[k]
                if val == arr[i]:
                    p = 1 if j == k else 2
                    dp[i] = (dp[i] + dp[j] * dp[k] * p) % mod
                    j += 1
                elif val > arr[i]:
                    k -= 1
                else:
                    j += 1
            res = (res + dp[i]) % mod
        return res
