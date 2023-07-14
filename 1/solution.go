package _1

func twoSum(nums []int, target int) []int {
	tmp := map[int]int{}
	for i, num := range nums {
		val := target - num
		idx, ok := tmp[num]
		if ok {
			return []int{idx, i}
		} else {
			tmp[val] = i
		}
	}
	return []int{}
}
