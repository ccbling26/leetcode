package _76

func minWindow(s string, t string) string {
	n := len(s)
	if n < len(t) {
		return ""
	}
	counter := map[byte]int{}
	i, j, p, q, count := 0, 0, 0, n+1, 0
	for i := 0; i < len(t); i++ {
		c := t[i]
		counter[c]++
		if counter[c] == 1 {
			count++
		}
	}
	for j < n {
		c := s[j]
		j++
		_, ok := counter[c]
		if ok {
			counter[c]--
			if counter[c] == 0 {
				count--
			}
		}
		for i < j && count == 0 {
			if q-p > j-i {
				q = j
				p = i
			}
			c = s[i]
			i++
			_, ok = counter[c]
			if ok {
				if counter[c] == 0 {
					count++
				}
				counter[c]++
			}
		}
	}
	if q == n+1 {
		return ""
	}
	return s[p:q]
}
