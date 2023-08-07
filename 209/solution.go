package _209

func minSubArrayLen(target int, nums []int) int {
	n := len(nums)
	res := len(nums) + 1
	i, j, total := 0, 0, 0
	min := func(a, b int) int {
		if a > b {
			return b
		}
		return a
	}
	for j < n {
		total += nums[j]
		j++
		for i < j && total >= target {
			res = min(res, j-i)
			total -= nums[i]
			i++
		}
	}
	if res == n+1 {
		res = 0
	}
	return res
}
