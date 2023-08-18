from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        mod = 10 ** 9 + 7
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        ans = [[[0] * (cols) for _ in range(rows)] for _ in range(k)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1] + (1 if pizza[i][j] == "A" else 0)
                ans[0][i][j] = 1 if dp[i][j] > 0 else 0

        for a in range(1, k):
            for b in range(rows):
                for c in range(cols):
                    for d in range(b + 1, rows):
                        if dp[b][c] == dp[d][c]:
                            continue
                        elif dp[d][c] == 0:
                            break
                        else:
                            ans[a][b][c] = (ans[a][b][c] + ans[a - 1][d][c]) % mod
                    for d in range(c + 1, cols):
                        if dp[b][c] == dp[b][d]:
                            continue
                        elif dp[b][d] == 0:
                            break
                        else:
                            ans[a][b][c] = (ans[a][b][c] + ans[a - 1][b][d]) % mod
        return ans[k - 1][0][0]
