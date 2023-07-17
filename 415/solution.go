package _415

import "strconv"

func addStrings(num1 string, num2 string) string {
	add := 0
	res := ""
	for i, j := len(num1)-1, len(num2)-1; i >= 0 || j >= 0 || add != 0; i, j = i-1, j-1 {
		val1 := 0
		val2 := 0
		if i >= 0 {
			val1 = int(num1[i] - '0')
		}
		if j >= 0 {
			val2 = int(num2[j] - '0')
		}
		total := val1 + val2 + add
		res = strconv.Itoa(total%10) + res
		add = total / 10
	}
	return res
}
