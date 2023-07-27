import java.util.Arrays;

class Solution {
    public int deleteGreatestValue(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int res = 0;
        for (int i = 0; i < m; i++) {
            Arrays.sort(grid[i]);
        }
        for (int i = 0; i < n; i++) {
            int mx = grid[0][i];
            for (int j = 1; j < m; j++) {
                mx = Math.max(mx, grid[j][i]);
            }
            res += mx;
        }
        return res;
    }
}