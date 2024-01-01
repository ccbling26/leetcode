class Solution {
    public int minOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        if (4 * boardingCost - runningCost <= 0) {
            return -1;
        }
        int minRound = 0, curRound = 0, maxProfits = 0, curProfits = 0, restNum = 0;
        int i = 0, n = customers.length;
        while (i < n || restNum > 0) {
            if (i < n) {
                restNum += customers[i];
                i++;
            }
            curProfits += Math.min(restNum, 4) * boardingCost - runningCost;
            curRound++;
            if (curProfits > maxProfits) {
                minRound = curRound;
                maxProfits = curProfits;
            }
            restNum -= Math.min(restNum, 4);
        }
        return minRound > 0 ? minRound : -1;
    }
}