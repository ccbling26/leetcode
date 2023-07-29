package _2050

func minimumTime(n int, relations [][]int, time []int) int {
	prev := make([][]int, n)
	for _, relation := range relations {
		x, y := relation[0], relation[1]
		prev[y-1] = append(prev[y-1], x-1)
	}
	dpDict := map[int]int{}

	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	var dp func(idx int) int
	dp = func(idx int) int {
		v, ok := dpDict[idx]
		if ok == true {
			return v
		}
		cur := 0
		for _, p := range prev[idx] {
			cur = max(cur, dp(p))
		}
		cur += time[idx]
		dpDict[idx] = cur
		return cur
	}

	res := 0
	for i := 0; i < n; i++ {
		res = max(res, dp(i))
	}
	return res
}
