package _20

func isValid(s string) bool {
	var q []rune
	relations := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}
	for _, c := range s {
		if c == '(' || c == '[' || c == '{' {
			q = append(q, c)
		} else if len(q) == 0 {
			return false
		} else if q[len(q)-1] == relations[c] {
			q = q[:len(q)-1]
		} else {
			return false
		}
	}
	return len(q) == 0
}
