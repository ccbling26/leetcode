class Solution {
    public int[] plusOne(int[] digits) {
        int added = 1;
        int idx = digits.length - 1;
        while (idx >= 0 && added != 0) {
            digits[idx] += added;
            added = digits[idx] / 10;
            digits[idx] %= 10;
            idx--;
        }
        if (added != 0) {
            int[] res = new int[digits.length + 1];
            res[0] = added;
            for (int i = 1; i <= digits.length; i++) {
                res[i] = digits[i - 1];
            }
            digits = res;
        }
        return digits;
    }
}