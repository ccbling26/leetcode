class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int n = nums.length;
        for (int i = 1; i < n; i++) {
            nums[i] += nums[i - 1];
        }
        int a = 0, b = 0;
        for (int i = 0; i < n; i++) {
            a = Math.max(a, nums[i]);
            b = Math.min(b, nums[i]);
        }
        return a - b;
    }
}