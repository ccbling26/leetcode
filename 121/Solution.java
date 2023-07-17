class Solution {
    public int maxProfit(int[] prices) {
        int minVal = 10000;
        int maxVal = 10000;
        int res = 0;
        for (int price: prices) {
            if (price < minVal) {
                maxVal = price;
                minVal = price;
            } else if (price > maxVal) {
                maxVal = price;
                res = Math.max(res, price - minVal);
            }
        }
        return res;
    }
}