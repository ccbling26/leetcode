class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length, total = 0, res = 0, idx = 0;
        for (int i = 0; i < n; i++) {
            int val = gas[i] - cost[i];
            total += val;
            res += val;
            if (res < 0) {
                res = 0;
                idx = i + 1;
            }
        }
        if (total < 0) {
            return -1;
        }
        return idx;
    }
}