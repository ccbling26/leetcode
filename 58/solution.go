package _58

func lengthOfLastWord(s string) int {
	n := len(s)
	i := n - 1
	for i >= 0 && s[i] == ' ' {
		i -= 1
	}
	j := i
	for j >= 0 && s[j] != ' ' {
		j -= 1
	}
	return i - j
}
