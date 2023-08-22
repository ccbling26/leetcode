class Solution {
    public int maxDistToClosest(int[] seats) {
        int i = -1, j = 0;
        int res = 0, n = seats.length;
        while (j < n) {
            while (j < n && seats[j] == 0) {
                j++;
            }
            if (i == -1) {
                res = j;
            } else if (j >= n) {
                res = Math.max(res, j - i - 1);
            } else {
                res = Math.max(res, (j - i) / 2);
            }
            i = j;
            j++;
        }
        return res;
    }
}