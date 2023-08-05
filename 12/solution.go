package _12

func intToRoman(num int) string {
	res := ""
	values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	symbols := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	for i := 0; i < len(values); i++ {
		for num >= values[i] {
			res += symbols[i]
			num -= values[i]
		}
		if num == 0 {
			break
		}
	}
	return res
}
