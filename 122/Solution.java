class Solution {
    public int maxProfit(int[] prices) {
        int sell = 0;
        int buy = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            int tmp = buy;
            buy = Math.max(buy, sell - prices[i]);
            sell = Math.max(sell, tmp + prices[i]);
        }
        return sell;
    }
}