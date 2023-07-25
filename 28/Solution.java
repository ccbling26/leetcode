class Solution {
    public int strStr(String haystack, String needle) {
        KMP kmp = new KMP(needle);
        return kmp.search(haystack);
    }
}

class KMP {
    private String pattern;
    private int m;
    private int[] dp;

    public KMP(String pattern) {
        this.pattern = pattern;
        this.m = pattern.length();
        this.dp = new int[this.m];
        int j = 0;
        for (int i = 1; i < this.m; i++) {
            while (j > 0 && this.pattern.charAt(i) != this.pattern.charAt(j)) {
                j = this.dp[j - 1];
            }
            if (this.pattern.charAt(i) == this.pattern.charAt(j)) {
                j++;
            }
            this.dp[i] = j;
        }
    }

    public int search(String txt) {
        int j = 0;
        for (int i = 0; i < txt.length(); i++) {
            while (j > 0 && txt.charAt(i) != this.pattern.charAt(j)) {
                j = this.dp[j - 1];
            }
            if (txt.charAt(i) == this.pattern.charAt(j)) {
                j++;
            }
            if (j == this.m) {
                return i - this.m + 1;
            }
        }
        return -1;
    }
}