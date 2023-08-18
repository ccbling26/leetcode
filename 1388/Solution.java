class Solution {
    public int maxSizeSlices(int[] slices) {
        int n = slices.length;
        int[] arr1 = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            arr1[i] = slices[i];
        }
        int ans = cal(arr1);
        for (int i = 0; i < n - 1; i++) {
            arr1[i] = slices[i + 1];
        }
        ans = Math.max(ans, cal(arr1));
        return ans;
    }

    private int cal(int[] slices) {
        int m = slices.length;
        int n = (m + 1) / 3;
        int[][] dp = new int[m][];
        for (int i = 0; i < m; i++) {
            dp[i] = new int[n + 1];
        }
        dp[0][1] = slices[0];
        dp[1][1] = Math.max(slices[0], slices[1]);
        for (int i = 2; i < m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = Math.max(dp[i - 2][j - 1] + slices[i], dp[i - 1][j]);
            }
        }
        return dp[m - 1][n];
    }
}