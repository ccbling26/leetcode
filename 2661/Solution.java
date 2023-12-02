import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length, n = mat[0].length;
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                hashMap.put(mat[i][j], i * n + j);
            }
        }
        int[] rows = new int[m];
        int[] cols = new int[n];
        Arrays.fill(rows, n);
        Arrays.fill(cols, m);
        for (int i = 0; i < arr.length; i++) {
            int index = hashMap.get(arr[i]);
            int row = index / n, col = index % n;
            rows[row]--;
            if (rows[row] == 0) {
                return i;
            }
            cols[col]--;
            if (cols[col] == 0) {
                return i;
            }
        }
        return -1;
    }
}