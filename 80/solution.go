package _80

func removeDuplicates(nums []int) int {
	idx := 0
	dup := false
	val := -10001
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[idx] = nums[i]
			idx += 1
			val = nums[i]
			dup = false
		} else if dup == false {
			nums[idx] = nums[i]
			idx += 1
			dup = true
		}
	}
	return idx
}
