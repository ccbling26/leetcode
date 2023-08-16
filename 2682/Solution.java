import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] circularGameLosers(int n, int k) {
        boolean[] flag = new boolean[n];
        int idx = 0;
        int step = k;
        flag[idx] = true;
        while (true) {
            idx = (idx + step) % n;
            if (flag[idx]) {
                break;
            }
            flag[idx] = true;
            step += k;
        }
        List<Integer> tmp = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!flag[i]) {
                tmp.add(i + 1);
            }
        }
        int[] res = new int[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            res[i] = tmp.get(i);
        }
        return res;
    }
}