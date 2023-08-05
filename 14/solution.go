package _14

func longestCommonPrefix(strs []string) string {
	n := len(strs)
	lengths := make([]int, n)
	for i := 0; i < n; i++ {
		lengths[i] = len(strs[i])
	}
	res := []byte{}
	i := 0
	l := 1
	cur := byte(' ')
	for true {
		if l > lengths[i] {
			break
		}
		if cur == ' ' {
			cur = strs[i][l-1]

		} else if strs[i][l-1] != cur {
			break
		}
		i += 1
		if i == n {
			i = 0
			res = append(res, cur)
			cur = ' '
			l += 1
		}

	}
	return string(res)

}
