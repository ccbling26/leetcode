class Solution {
    private int[] nums;
    private int target;

    public int searchInsert(int[] nums, int target) {
        this.nums = nums;
        this.target = target;
        return find(0, nums.length - 1);
    }

    public int find(int l, int r) {
        if (l > r) {
            return l;
        }
        int mid = (l + r) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            return find(l, mid - 1);
        } else {
            return find(mid + 1, r);
        }
    }
}