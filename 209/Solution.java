class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int i = 0, j = 0;
        int total = 0;
        int res = n + 1;
        while (j < n) {
            total += nums[j];
            j++;
            while (total >= target) {
                res = Math.min(res, j - i);
                total -= nums[i];
                i++;
            }
        }
        return res == n + 1 ? 0 : res;
    }
}