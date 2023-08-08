package main

func maxAbsoluteSum(nums []int) int {
	n := len(nums)
	for i := 1; i < n; i++ {
		nums[i] += nums[i-1]
	}
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	a, b := 0, 0
	for i := 0; i < n; i++ {
		a = max(a, nums[i])
		b = min(b, nums[i])
	}
	return a - b
}
