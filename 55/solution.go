package _55

func canJump(nums []int) bool {
	rightMost := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		if i <= rightMost {
			rightMost = max(rightMost, i+nums[i])
		} else {
			return false
		}
		if rightMost >= n-1 {
			return true
		}
	}
	return true
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
