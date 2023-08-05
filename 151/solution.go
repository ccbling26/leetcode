package _151

func reverseWords(s string) string {
	sList := []byte(s)

	reverse := func(x, y int) {
		for x < y {
			sList[x], sList[y] = sList[y], sList[x]
			x++
			y--
		}
	}

	n, i, j, l := len(s), 0, 0, 0
	reverse(0, n-1)
	for j < n {
		if sList[j] != ' ' {
			i = j
			if l != 0 {
				sList[l] = ' '
				l++
			}
			for j < n && sList[j] != ' ' {
				sList[l] = sList[j]
				j++
				l++
			}
			reverse(l-j+i, l-1)
		}
		j++
	}
	return string(sList[:l])
}
