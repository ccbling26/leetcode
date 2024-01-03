import java.util.HashMap;
import java.util.Map;

class Solution {
    public int getMaxRepetitions(String s1, int n1, String s2, int n2) {
        if (n1 == 0) {
            return 0;
        }
        int s1Cnt = 0, s2Cnt = 0, idx = 0;
        Map<Integer, int[]> recall = new HashMap<Integer, int[]>();
        int[] preLoop = new int[2];
        int[] inLoop = new int[2];
        while (true) {
            s1Cnt++;
            for (int i = 0; i < s1.length(); i++) {
                char ch = s1.charAt(i);
                if (ch == s2.charAt(idx)) {
                    idx++;
                    if (idx == s2.length()) {
                        s2Cnt++;
                        idx = 0;
                    }
                }
            }
            if (s1Cnt == n1) {
                return s2Cnt / n2;
            }
            if (recall.containsKey(idx)) {
                int[] val = recall.get(idx);
                preLoop[0] = val[0];
                preLoop[1] = val[1];
                inLoop[0] = s1Cnt - val[0];
                inLoop[1] = s2Cnt - val[1];
                break;
            } else {
                recall.put(idx, new int[]{s1Cnt, s2Cnt});
            }
        }
        int ans = preLoop[1] + (n1 - preLoop[0]) / inLoop[0] * inLoop[1];
        int rest = (n1 - preLoop[0]) % inLoop[0];
        for (int i = 0; i < rest; i++) {
            for (int j = 0; j < s1.length(); j++) {
                char ch = s1.charAt(j);
                if (ch == s2.charAt(idx)) {
                    idx++;
                    if (idx == s2.length()) {
                        ans++;
                        idx = 0;
                    }
                }
            }
        }
        return ans / n2;
    }
}