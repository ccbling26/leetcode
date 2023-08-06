package _392

func isSubsequence(s string, t string) bool {
	i, j, l1, l2 := 0, 0, len(s), len(t)
	for i < l1 && j < l2 {
		if s[i] == t[j] {
			i++
		}
		j++
	}
	return i == l1
}
