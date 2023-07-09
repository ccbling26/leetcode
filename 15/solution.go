package _15

import "sort"

type IntSlice []int

func (s IntSlice) Len() int           { return len(s) }
func (s IntSlice) Less(i, j int) bool { return s[i] < s[j] }
func (s IntSlice) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

func threeSum(nums []int) [][]int {
	n := len(nums)
	if n < 3 {
		return [][]int{}
	}
	sort.Sort(IntSlice(nums))
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
