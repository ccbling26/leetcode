package _5

func longestPalindrome(s string) string {
	n, length := len(s), 1
	begin, end := 0, 0
	find := func(i, j int) {
		for i >= 0 && j < n {
			if s[i] != s[j] {
				break
			}
			i--
			j++
		}
		if j-i-1 > length {
			length = j - i - 1
			begin = i + 1
			end = j - 1
		}
	}
	for i := 0; i < n; i++ {
		find(i, i)
		find(i, i+1)
	}
	return s[begin : end+1]
}
