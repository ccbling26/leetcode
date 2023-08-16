package _2682

func circularGameLosers(n int, k int) []int {
	flag := make([]bool, n)
	idx := 0
	step := k
	flag[idx] = true
	for {
		idx = (idx + step) % n
		if flag[idx] {
			break
		}
		flag[idx] = true
		step += k
	}
	res := []int{}
	for i := 0; i < n; i++ {
		if !flag[i] {
			res = append(res, i+1)
		}
	}
	return res
}
