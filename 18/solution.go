package _18

import "sort"

func fourSum(nums []int, target int) [][]int {
	n := len(nums)
	if n < 4 {
		return [][]int{}
	}
	res := [][]int{}
	sort.Sort(sort.IntSlice(nums))
	for i := 0; i < n-3; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target {
			break
		} else if nums[i]+nums[n-1]+nums[n-2]+nums[n-3] < target {
			continue
		}
		for j := i + 1; j < n-2; j++ {
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}
			if nums[i]+nums[j]+nums[j+1]+nums[j+2] > target {
				break
			} else if nums[i]+nums[j]+nums[n-1]+nums[n-2] < target {
				continue
			}
			l := j + 1
			r := n - 1
			for l < r {
				val := nums[i] + nums[j] + nums[l] + nums[r]
				if val < target {
					l += 1
				} else if val > target {
					r -= 1
				} else {
					res = append(res, []int{nums[i], nums[j], nums[l], nums[r]})
					for l < r && nums[l] == nums[l+1] {
						l += 1
					}
					for l < r && nums[r] == nums[r-1] {
						r -= 1
					}
					l += 1
					r -= 1
				}
			}
		}
	}
	return res
}
