class Solution {
    public boolean canJump(int[] nums) {
        int rightMost = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (i <= rightMost) {
                rightMost = Math.max(rightMost, i + nums[i]);
            } else {
                return false;
            }
            if (rightMost >= n - 1) {
                return true;
            }
        }
        return true;
    }
}