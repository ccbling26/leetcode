package _13

func romanToInt(s string) int {
	dic := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	var pre rune
	res := 0
	for _, c := range s {
		if c == 'I' {
			res++
		} else if c == 'V' || c == 'X' {
			res += dic[c]
			if pre == 'I' {
				res -= 2 * dic['I']
			}
		} else if c == 'L' || c == 'C' {
			res += dic[c]
			if pre == 'X' {
				res -= 2 * dic['X']
			}
		} else {
			res += dic[c]
			if pre == 'C' {
				res -= 2 * dic['C']
			}
		}
		pre = c
	}
	return res
}
