class Solution {
    private int[] nums;

    private void reverse(int l, int h) {
        while (l < h) {
            int tmp = nums[l];
            nums[l] = nums[h];
            nums[h] = tmp;
            l++;
            h--;
        }
    }

    public void rotate(int[] nums, int k) {
        this.nums = nums;
        int n = nums.length;
        k %= n;
        reverse(0, n - 1);
        reverse(0, k - 1);
        reverse(k, n - 1);
    }
}