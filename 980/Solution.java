import java.util.HashMap;

class Solution {
    private int m;
    private int n;
    private int[][] grid;
    private static int[][] cases = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
    private HashMap<Integer, Integer> cache = new HashMap<>();

    public int uniquePathsIII(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        this.grid = grid;

        int si = 0, sj = 0, st = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    si = i;
                    sj = j;
                } else if (grid[i][j] == 0 || grid[i][j] == 2) {
                    st |= (1 << (i * n + j));
                }
            }
        }
        return find(si, sj, st);
    }

    private int find(int i, int j, int st) {
        if (grid[i][j] == 2) {
            if (st == 0) {
                return 1;
            }
            return 0;
        }
        int key = ((i * n + j) << (m * n)) + st;
        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        int res = 0;
        for (int[] item : cases) {
            int ti = i + item[0], tj = j + item[1];
            if (ti >= 0 && ti < m && tj >= 0 && tj < n && ((st >> (ti * n + tj)) & 1) == 1) {
                res += find(ti, tj, st ^ (1 << (ti * n + tj)));
            }
        }
        cache.put(key, res);
        return res;
    }
}