class Solution {
    public long maxAlternatingSum(int[] nums) {
        long even = 0;
        long odd = 0;
        for (int i = 0; i < nums.length; i++) {
            long tmp1 = Math.max(even, odd + nums[i]);
            long tmp2 = Math.max(odd, even - nums[i]);
            even = tmp1;
            odd = tmp2;
        }
        return even;
    }
}