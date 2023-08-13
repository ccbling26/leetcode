class Solution {
    public int mySqrt(int x) {
        int l = 0, r = x;
        while (l <= r) {
            int mid = (l + r) / 2;
            long val = (long) mid * mid;
            if (val == x) {
                return mid;
            } else if (val < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r;
    }
}