package _2681

import "sort"

func sumOfPower(nums []int) int {
	mod := int(1e9 + 7)
	n := len(nums)
	sort.Ints(nums)
	res := 0
	dp := 0
	preSum := 0
	for i := 0; i < n; i++ {
		dp = (preSum + nums[i]) % mod
		preSum = (preSum + dp) % mod
		res = (res + (dp*nums[i]%mod)*nums[i]%mod) % mod
	}
	return res
}
