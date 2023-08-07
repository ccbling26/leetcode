import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 1;
        int n = s.length();
        int i = 0, j = 0;
        HashSet<Character> hashSet = new HashSet<>();
        while (j < n) {
            char c = s.charAt(j);
            while (hashSet.contains(c)) {
                hashSet.remove(s.charAt(i));
                i++;
            }
            hashSet.add(c);
            j++;
            res = Math.max(res, j - i);
        }
        return res;
    }
}