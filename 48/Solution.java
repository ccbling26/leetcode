class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        for (int i = 0; i < n; i++) {
            int j = 0, k = n - 1;
            while (j < k) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][k];
                matrix[i][k] = tmp;
                j++;
                k--;
            }
        }
    }
}