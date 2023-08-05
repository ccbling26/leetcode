class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        StringBuilder[] arr = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            arr[i] = new StringBuilder();
        }
        int cur = 0, flag = -1;
        for (char c : s.toCharArray()) {
            arr[cur].append(c);
            if (cur == 0 || cur == numRows - 1) {
                flag *= -1;
            }
            cur += flag;
        }
        StringBuilder res = new StringBuilder();
        for (StringBuilder item : arr) {
            res.append(item);
        }
        return res.toString();
    }
}