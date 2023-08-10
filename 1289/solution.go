package _1289

import "math"

func minFallingPathSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	res := [3]int{0, -1, 0}
	tmp := [3]int{math.MaxInt, -1, math.MaxInt}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j != res[1] {
				grid[i][j] += res[0]
			} else {
				grid[i][j] += res[2]
			}
			if grid[i][j] <= tmp[0] {
				tmp[2] = tmp[0]
				tmp[1] = j
				tmp[0] = grid[i][j]
			} else if grid[i][j] < tmp[2] {
				tmp[2] = grid[i][j]
			}
		}
		res = tmp
		tmp = [3]int{math.MaxInt, -1, math.MaxInt}
	}
	return res[0]
}
