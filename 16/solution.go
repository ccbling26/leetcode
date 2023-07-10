package _16

import (
	"math"
	"sort"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func threeSumClosest(nums []int, target int) int {
	sort.Sort(sort.IntSlice(nums))
	n := len(nums)
	res := math.MaxInt
	for i := 0; i < n; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l := i + 1
		r := n - 1
		for l < r {
			tmp := nums[i] + nums[l] + nums[r]
			if tmp == target {
				return tmp
			}
			if abs(tmp-target) < abs(res-target) {
				res = tmp
			}
			if tmp < target {
				for l < r && nums[l] == nums[l+1] {
					l++
				}
				l++
			} else {
				for l < r && nums[r] == nums[r-1] {
					r--
				}
				r--
			}
		}
	}
	return res
}
