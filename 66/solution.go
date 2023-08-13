package _66

func plusOne(digits []int) []int {
	added := 1
	idx := len(digits) - 1
	for idx >= 0 && added != 0 {
		digits[idx] += added
		added = digits[idx] / 10
		digits[idx] %= 10
		idx--
	}
	if added != 0 {
		res := []int{added}
		digits = append(res, digits...)
	}
	return digits
}
