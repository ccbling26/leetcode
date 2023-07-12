class Solution {
    public int alternateDigitSum(int n) {
        int sign = 1;
        int res = 0;
        while (n > 0) {
            res += n % 10 * sign;
            sign *= -1;
            n /= 10;
        }
        return -1 * sign * res;
    }
}