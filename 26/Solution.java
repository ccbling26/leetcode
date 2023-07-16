class Solution {
    public int removeDuplicates(int[] nums) {
        int idx = 0;
        int val = -1 * (int) Math.pow(10, 4) - 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[idx] = nums[i];
                val = nums[i];
                idx++;
            }
        }
        return idx;
    }
}