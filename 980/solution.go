package _980

func uniquePathsIII(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	si, sj, st := 0, 0, 0
	cache := map[int]int{}
	cases := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				si, sj = i, j
			} else if grid[i][j] == 0 || grid[i][j] == 2 {
				st |= (1 << (n*i + j))
			}
		}
	}

	var find func(x int, y int, z int) int
	find = func(x int, y int, z int) int {
		if grid[x][y] == 2 {
			if z == 0 {
				return 1
			}
			return 0
		}
		key := ((x*n + y) << (m * n)) + z
		res, ok := cache[key]
		if !ok {
			res = 0
			for _, c := range cases {
				ti, tj := x+c[0], y+c[1]
				if ti >= 0 && ti < m && tj >= 0 && tj < n && (z&(1<<(n*ti+tj))) > 0 {
					res += find(ti, tj, z^(1<<(n*ti+tj)))
				}
			}
			cache[key] = res
		}
		return res
	}
	return find(si, sj, st)
}
