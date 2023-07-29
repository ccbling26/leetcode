import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    private int[] time;
    public List<List<Integer>> prev;
    public HashMap<Integer, Integer> dpDict;

    public int minimumTime(int n, int[][] relations, int[] time) {
        this.time = time;
        prev = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            prev.add(new ArrayList<>());
        }
        for (int[] relation : relations) {
            int x = relation[0] - 1, y = relation[1] - 1;
            prev.get(y).add(x);
        }
        dpDict = new HashMap<>();
        int res = 0;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, dp(i));
        }
        return res;
    }

    public int dp(int idx) {
        if (dpDict.containsKey(idx)) {
            return dpDict.get(idx);
        }
        int cur = 0;
        for (int p : prev.get(idx)) {
            cur = Math.max(cur, dp(p));
        }
        cur += time[idx];
        dpDict.put(idx, cur);
        return cur;
    }
}