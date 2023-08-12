import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        int n = s.length();
        if (n < t.length()) {
            return "";
        }
        HashMap<Character, Integer> collector = new HashMap<>();
        int i = 0, j = 0, p = 0, q = n + 1, count = 0;
        for (char c : t.toCharArray()) {
            if (collector.containsKey(c)) {
                collector.put(c, collector.get(c) + 1);
            } else {
                collector.put(c, 1);
                count++;
            }
        }
        while (j < n) {
            char c = s.charAt(j);
            j++;
            if (collector.containsKey(c)) {
                collector.put(c, collector.get(c) - 1);
                if (collector.get(c) == 0) {
                    count--;
                }
            }
            while (i < j && count == 0) {
                if (q - p > j - i) {
                    q = j;
                    p = i;
                }
                c = s.charAt(i);
                if (collector.containsKey(c)) {
                    if (collector.get(c) == 0) {
                        count++;
                    }
                    collector.put(c, collector.get(c) + 1);
                }
                i++;
            }
        }
        if (q == n + 1) {
            return "";
        }
        return s.substring(p, q);
    }
}