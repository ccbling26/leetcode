package _849

func maxDistToClosest(seats []int) int {
	i, j := -1, 0
	res, n := 0, len(seats)
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	for j < n {
		for j < n && seats[j] == 0 {
			j++
		}
		if i == -1 {
			res = j
		} else if j >= n {
			res = max(res, j-i-1)
		} else {
			res = max(res, (j-i)/2)
		}
		i = j
		j++
	}
	return res
}
