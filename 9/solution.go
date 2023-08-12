package _9

func isPalindrome(x int) bool {
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}
	y := 0
	for y < x {
		y *= 10
		y += x % 10
		x /= 10
	}
	return y == x || x == y/10
}
