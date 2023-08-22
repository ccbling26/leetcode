import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int a = 0, b = n - 1, c = 0, d = m - 1;
        List<Integer> res = new ArrayList<>();
        while(a <= b && c <= d) {
            for(int i = a; i <= b; i++) {
                res.add(matrix[c][i]);
            }
            c++;
            for(int i = c; i <= d; i++) {
                res.add(matrix[i][b]);
            }
            b--;
            if (a > b || c > d) {
                break;
            }
            for(int i = b; i >= a; i--) {
                res.add(matrix[d][i]);
            }
            d--;
            for(int i = d; i >= c; i--) {
                res.add(matrix[i][a]);
            }
            a++;
        }
        return res;
    }
}