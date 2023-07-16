package _26

import "math"

func removeDuplicates(nums []int) int {
	val := -1 * int(math.Pow(10, 4))
	idx := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[idx] = nums[i]
			val = nums[i]
			idx += 1
		}
	}
	return idx
}
