package _1911

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxAlternatingSum(nums []int) int64 {
	even := 0
	odd := 0
	for _, num := range nums {
		even, odd = max(even, odd+num), max(odd, even-num)
	}
	return int64(even)
}
