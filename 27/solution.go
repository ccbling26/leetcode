package _27

func removeElement(nums []int, val int) int {
	idx := 0
	count := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			nums[idx] = nums[i]
			idx++
			count++
		}
	}
	return count
}
