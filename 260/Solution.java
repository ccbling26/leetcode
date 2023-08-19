class Solution {
    public int[] singleNumber(int[] nums) {
        int tmp = 0;
        for (int num : nums) {
            tmp ^= num;
        }
        int i = 1;
        while ((i & tmp) == 0) {
            i <<= 1;
        }
        int a = 0, b = 0;
        for (int num : nums) {
            if ((num & i) > 0) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        return new int[] { a, b };
    }
}