import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> tmp = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int val = target - num;
            if (tmp.containsKey(num)) {
                return new int[]{tmp.get(num), i};
            } else {
                tmp.put(val, i);
            }
        }
        return new int[]{};
    }
}