class Solution {
    public int minFallingPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] res = new int[]{0, -1, 0};
        int[] tmp = new int[]{Integer.MAX_VALUE, -1, Integer.MAX_VALUE};
        for (int i = 0;i<m;i++) {
            for (int j = 0;j<n;j++) {
                if (j != res[1]) {
                    grid[i][j] += res[0];
                } else {
                    grid[i][j] += res[2];
                }
                if (grid[i][j] <= tmp[0]) {
                    tmp[2] = tmp[0];
                    tmp[1] = j;
                    tmp[0] = grid[i][j];
                } else if (grid[i][j] < tmp[2]) {
                    tmp[2] = grid[i][j];
                }
            }
            res = tmp;
            tmp = new int[]{Integer.MAX_VALUE, -1, Integer.MAX_VALUE};
        }
        return res[0];
    }
}