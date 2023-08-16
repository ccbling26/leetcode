class Solution {
    private String s;
    private int n;
    private int length = 1;
    private int begin = 0;
    private int end = 0;

    private void cal(int i, int j) {
        while (i >= 0 && j < n) {
            if (s.charAt(i) != s.charAt(j)) {
                break;
            }
            i--;
            j++;
        }
        if (j - i - 1 > length) {
            length = j - i - 1;
            begin = i + 1;
            end = j - 1;
        }
    }

    public String longestPalindrome(String s) {
        this.s = s;
        n = s.length();
        for (int i = 0; i < n; i++) {
            cal(i, i);
            cal(i, i + 1);
        }
        return s.substring(begin, end + 1);
    }
}