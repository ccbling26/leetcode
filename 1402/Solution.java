import java.util.Arrays;

class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        Arrays.sort(satisfaction);
        int preSum = 0, ans = 0;
        for (int i = satisfaction.length - 1; i >= 0; i--) {
            preSum += satisfaction[i];
            if (preSum > 0) {
                ans += preSum;
            } else
                break;
        }
        return ans;
    }
}
