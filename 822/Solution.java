import java.util.HashSet;

class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        HashSet<Integer> same = new HashSet<>();
        HashSet<Integer> keys = new HashSet<>();
        for (int i = 0; i < fronts.length; i++) {
            if (fronts[i] == backs[i]) {
                same.add(fronts[i]);
            } else {
                keys.add(fronts[i]);
                keys.add(backs[i]);
            }
        }
        int res = 2001;
        Integer[] keyList = keys.toArray(new Integer[keys.size()]);
        for (Integer key : keyList) {
            if (!same.contains(key)) {
                res = Math.min(res, key);
            }
        }
        return res == 2001 ? 0 : res;
    }
}
