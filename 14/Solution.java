class Solution {
    public String longestCommonPrefix(String[] strs) {
        int n = strs.length;
        int[] lengths = new int[n];
        for (int i = 0; i < n; i++) {
            lengths[i] = strs[i].length();
        }

        StringBuilder stringBuilder = new StringBuilder();
        int i = 0;
        int l = 1;
        char cur = ' ';
        while (true) {
            if (l > lengths[i]) {
                break;
            }
            if (cur == ' ') {
                cur = strs[i].charAt(l - 1);
            } else if (strs[i].charAt(l - 1) != cur) {
                break;
            }
            i++;
            if (i == n) {
                i = 0;
                stringBuilder.append(cur);
                cur = ' ';
                l++;
            }
        }
        return stringBuilder.toString();
    }
}