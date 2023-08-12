package _67

func addBinary(a string, b string) string {
	res := ""
	i := len(a) - 1
	j := len(b) - 1
	added := 0
	for i >= 0 || j >= 0 {
		if i >= 0 {
			added += int(a[i] - '0')
			i--
		}
		if j >= 0 {
			added += int(b[j] - '0')
			j--
		}
		res = string(rune(added%2+'0')) + res
		added /= 2
	}
	if added == 1 {
		res = "1" + res
	}
	return res
}
