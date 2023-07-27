package _2500

import "sort"

func deleteGreatestValue(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	res := 0
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	for i := 0; i < m; i++ {
		sort.Slice(grid[i], func(a, b int) bool {
			return grid[i][a] > grid[i][b]
		})
	}
	for i := 0; i < n; i++ {
		tmp := grid[0][i]
		for j := 1; j < m; j++ {
			tmp = max(tmp, grid[j][i])
		}
		res += tmp
	}
	return res
}
