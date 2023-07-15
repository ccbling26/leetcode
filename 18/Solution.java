import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int n = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        if (n < 4) {
            return res;
        }
        Arrays.sort(nums);
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            } else if ((long) nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) {
                break;
            } else if ((long) nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target) {
                continue;
            }
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                } else if ((long) nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) {
                    break;
                } else if ((long) nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target) {
                    continue;
                }
                int l = j + 1;
                int r = n - 1;
                while (l < r) {
                    long val = nums[i] + nums[j] + nums[l] + nums[r];
                    if (val < target) {
                        l++;
                    } else if (val > target) {
                        r--;
                    } else {
                        res.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[l], nums[r])));
                        while (l < r && nums[l] == nums[l + 1]) {
                            l++;
                        }
                        while (l < r && nums[r] == nums[r - 1]) {
                            r--;
                        } 
                        l++;
                        r--;
                    }
                }
            }
        }
        return res;
    }
}