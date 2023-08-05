class Solution {
    public int lengthOfLastWord(String s) {
        int n = s.length();
        int i = n - 1;
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }
        int j = i;
        while (j >= 0 && s.charAt(j) != ' ') {
            j--;
        }
        return i - j;
    }
}