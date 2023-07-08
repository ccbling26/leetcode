package _167

func twoSum(numbers []int, target int) []int {
	i := 0
	j := len(numbers) - 1
	for i < j {
		tmp := numbers[i] + numbers[j]
		if tmp == target {
			return []int{i + 1, j + 1}
		} else if tmp > target {
			j--
		} else {
			i++
		}
	}
	return []int{}
}
