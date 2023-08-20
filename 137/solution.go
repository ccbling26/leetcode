package _137

func singleNumber(nums []int) int {
	a, b := 0, 0
	for _, num := range nums {
		b = ^a & (b ^ num)
		a = ^b & (a ^ num)
	}
	return b
}
