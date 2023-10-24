class Solution {
    static final int mod = 1000000007;

    public int numRollsToTarget(int n, int k, int target) {
        if (n > target) {
            return 0;
        } else if (n == target) {
            return 1;
        }
        int[][] dp = new int[n][target];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[target];
        }
        for (int i = 0; i < Math.min(target, k); i++) {
            dp[0][i] = 1;
        }
        for (int i = 1; i < n; i++) {
            dp[i][i] = 1;
            for (int j = i + 1; j < Math.min(target, k * (i + 1)); j++) {
                for (int l = j - 1; l >= Math.max(i - 1, j - k); l--) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][l]) % mod;
                }
            }
        }
        return dp[n - 1][target - 1];
    }
}