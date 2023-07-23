class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        res[0] = nums[0];
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i];
        }
        for (int i = n - 2; i >= 0; i--) {
            nums[i] *= nums[i + 1];
        }
        res[n - 1] = res[n - 2];
        for (int i = n - 2; i > 0; i--) {
            res[i] = res[i - 1] * nums[i + 1];
        }
        res[0] = nums[1];
        return res;
    }
}