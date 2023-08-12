class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        StringBuilder res = new StringBuilder();
        int added = 0;
        while (i >= 0 || j >= 0) {
            if (i >= 0) {
                added += a.charAt(i);
                i--;
            }
            if (j >= 0) {
                added += b.charAt(j) - '0';
                j--;
            }
            res.append(Integer.toString(added % 2));
            added /= 2;
        }
        if (added == 1) {
            res.append('1');
        }
        return res.reverse().toString();
    }
}