package _122

func maxProfit(prices []int) int {
	sell := 0
	buy := -prices[0]
	for i := 1; i < len(prices); i++ {
		tmp := buy
		buy = max(buy, sell-prices[i])
		sell = max(sell, tmp+prices[i])
	}
	return sell
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
