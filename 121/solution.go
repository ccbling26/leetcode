package _121

func maxProfit(prices []int) int {
	minVal := 10000
	maxVal := 10000
	res := 0
	for _, price := range prices {
		if price < minVal {
			minVal = price
			maxVal = price
		} else if price > maxVal {
			maxVal = price
			res = max(res, maxVal-minVal)
		}
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
