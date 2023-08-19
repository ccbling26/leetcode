package _260

func singleNumber(nums []int) []int {
	tmp := 0
	for _, num := range nums {
		tmp ^= num
	}
	i := 1
	for i&tmp == 0 {
		i <<= 1
	}
	a := 0
	b := 0
	for _, num := range nums {
		if num&i == 0 {
			b ^= num
		} else {
			a ^= num
		}
	}
	return []int{a, b}
}
