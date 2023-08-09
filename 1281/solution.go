package _1281

func subtractProductAndSum(n int) int {
	a, b := 1, 0
	for n > 0 {
		c := n % 10
		n /= 10
		a *= c
		b += c
	}
	return a - b
}
