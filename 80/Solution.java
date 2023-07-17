class Solution {
    public int removeDuplicates(int[] nums) {
        int idx = 0;
        boolean dup = false;
        int val = -10001;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == val && dup == true) {
                continue;
            } else if (nums[i] != val) {
                dup = false;
            } else {
                dup = true;
            }
            nums[idx] = nums[i];
            val = nums[i];
            idx++;
        }
        return idx;
    }
}