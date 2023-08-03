package _822

func flipgame(fronts []int, backs []int) int {
	same := map[int]struct{}{}
	keys := map[int]struct{}{}
	for i, v1 := range fronts {
		v2 := backs[i]
		if v1 == v2 {
			same[v1] = struct{}{}
		} else {
			keys[v1] = struct{}{}
			keys[v2] = struct{}{}
		}
	}
	res := 2001
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	for k, _ := range keys {
		_, ok := same[k]
		if !ok {
			res = min(res, k)
		}
	}
	if res == 2001 {
		res = 0
	}
	return res
}
