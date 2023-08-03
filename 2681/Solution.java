import java.util.Arrays;

class Solution {
    public int sumOfPower(int[] nums) {
        int n = nums.length;
        int mod = 1000000007;
        int res = 0, dp = 0, preSum = 0;
        Arrays.sort(nums);
        for (int i = 0; i < n; i++) {
            dp = (nums[i] + preSum) % mod;
            preSum = (preSum + dp) % mod;
            res = (int) ((res + (long) nums[i] * nums[i] % mod * dp) % mod);
            if (res < 0) {
                res += mod;
            }
        }
        return res;
    }
}