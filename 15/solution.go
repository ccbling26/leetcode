package _15

import "sort"

func threeSum(nums []int) [][]int {
	n := len(nums)
	if n < 3 {
		return [][]int{}
	}
	sort.Sort(sort.IntSlice(nums))
	i := 0
	res := [][]int{}
	for i < n {
		if nums[i] > 0 {
			return res
		}
		if i == 0 || nums[i] != nums[i-1] {
			l := i + 1
			r := n - 1
			for l < r {
				total := nums[i] + nums[l] + nums[r]
				if total > 0 {
					r--
				} else if total < 0 {
					l++
				} else {
					res = append(res, []int{nums[i], nums[l], nums[r]})
					for l < r && nums[l] == nums[l+1] {
						l++
					}
					for l < r && nums[r] == nums[r-1] {
						r--
					}
					l++
					r--
				}
			}
		}
		i++
	}
	return res
}
