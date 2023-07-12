package _2544

func alternateDigitSum(n int) int {
	sign := 1
	res := 0
	for n > 0 {
		res += n % 10 * sign
		sign *= -1
		n /= 10
	}
	return -1 * sign * res
}
