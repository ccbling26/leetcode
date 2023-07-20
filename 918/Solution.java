class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int n = nums.length;
        int maxPre = nums[0], maxRes = nums[0];
        int minPre = nums[0], minRes = nums[0];
        int total = nums[0];
        for (int i = 1; i < n; i++) {
            maxPre = Math.max(maxPre + nums[i], nums[i]);
            maxRes = Math.max(maxRes, maxPre);
            minPre = Math.min(minPre + nums[i], nums[i]);
            minRes = Math.min(minRes, minPre);
            total += nums[i];
        }
        if (maxRes < 0) {
            return maxRes;
        } else {
            return Math.max(maxRes, total - minRes);
        }
    }
}