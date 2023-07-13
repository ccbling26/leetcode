class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[][] dp = new int[n][n + 2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n + 2; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        for (int j = 1; j < n + 1; j++) {
            dp[0][j] = matrix[0][j - 1];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n + 1; j++) {
                dp[i][j] = matrix[i][j - 1] + Math.min(Math.min(dp[i - 1][j - 1], dp[i - 1][j]), dp[i - 1][j + 1]);
            }
        }
        int res = Integer.MAX_VALUE;
        for (int j = 1; j < n + 1; j++) {
            res = Math.min(res, dp[n - 1][j]);
        }
        return res;
    }
}