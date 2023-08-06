class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0, l1 = s.length(), l2 = t.length();
        while (i < l1 && j < l2) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == l1;
    }
}