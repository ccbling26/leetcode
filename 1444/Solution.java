class Solution {
    public int ways(String[] pizza, int k) {
        int m = pizza.length, n = pizza[0].length();
        int mod = 1000000007;
        int[][] dp = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            dp[i] = new int[n + 1];
        }
        int[][][] ans = new int[k][][];
        for (int i = 0; i < k; i++) {
            ans[i] = new int[m][];
            for (int j = 0; j < m; j++) {
                ans[i][j] = new int[n];
            }
        }
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1] + (pizza[i].charAt(j) == 'A' ? 1 : 0);
                ans[0][i][j] = dp[i][j] > 0 ? 1 : 0;
            }
        }
        for (int a = 1; a < k; a++) {
            for (int b = 0; b < m; b++) {
                for (int c = 0; c < n; c++) {
                    for (int d = b + 1; d < m; d++) {
                        if (dp[b][c] == dp[d][c]) {
                            continue;
                        } else if (dp[d][c] == 0) {
                            break;
                        } else {
                            ans[a][b][c] = (ans[a][b][c] + ans[a - 1][d][c]) % mod;
                        }
                    }
                    for (int d = c + 1; d < n; d++) {
                        if (dp[b][c] == dp[b][d]) {
                            continue;
                        } else if (dp[b][d] == 0) {
                            break;
                        } else {
                            ans[a][b][c] = (ans[a][b][c] + ans[a - 1][b][d]) % mod;
                        }
                    }
                }
            }
        }
        return ans[k - 1][0][0];
    }
}