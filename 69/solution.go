package _69

func mySqrt(x int) int {
	l, r := 0, x
	for l <= r {
		mid := (l + r) / 2
		val := mid * mid
		if val == x {
			return mid
		} else if val < x {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return r
}
