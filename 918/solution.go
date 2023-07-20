package _918

func maxSubarraySumCircular(nums []int) int {
	n := len(nums)
	preMax := nums[0]
	curMax := nums[0]
	preMin := nums[0]
	curMin := nums[0]
	total := nums[0]
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	min := func(a, b int) int {
		if a > b {
			return b
		}
		return a
	}
	for i := 1; i < n; i++ {
		preMax = max(preMax+nums[i], nums[i])
		curMax = max(curMax, preMax)
		preMin = min(preMin+nums[i], nums[i])
		curMin = min(curMin, preMin)
		total += nums[i]
	}
	if curMax < 0 {
		return curMax
	} else {
		return max(curMax, total-curMin)
	}
}
