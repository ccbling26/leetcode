package _274

func hIndex(citations []int) int {
	n := len(citations)
	counter := make([]int, n+1)
	for _, c := range citations {
		if c >= n {
			counter[n]++
		} else {
			counter[c]++
		}
	}
	res := 0
	for i := n; i >= 0; i-- {
		res += counter[i]
		if res >= i {
			return i
		}
	}
	return 0
}
