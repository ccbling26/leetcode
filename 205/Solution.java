import java.util.HashMap;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> relations1 = new HashMap<>();
        HashMap<Character, Character> relations2 = new HashMap<>();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char x = s.charAt(i);
            char y = t.charAt(i);
            if (relations1.containsKey(x)) {
                if (relations1.get(x) != y) {
                    return false;
                }
            } else if (relations2.containsKey(y)) {
                if (relations2.get(y) != x) {
                    return false;
                }
            } else {
                relations1.put(x, y);
                relations2.put(y, x);
            }
        }
        return true;
    }
}