class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        mem = [[-1] * n for _ in range(m)]

        def dp(i: int, j: int):
            if j >= n:
                return 1
            elif m - i < n - j:
                return 0
            if mem[i][j] != -1:
                return mem[i][j]
            res = dp(i + 1, j)
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            mem[i][j] = res
            return res

        return dp(0, 0)
