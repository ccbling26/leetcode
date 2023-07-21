package _874

func robotSim(commands []int, obstacles [][]int) int {
	dirs := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	x := 0
	y := 0
	d := 0
	res := 0
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	obstaclesMap := make(map[[2]int]struct{})
	for _, obstacle := range obstacles {
		obstaclesMap[[2]int{obstacle[0], obstacle[1]}] = struct{}{}
	}
	for _, command := range commands {
		if command == -2 {
			d = (d + 3) % 4
		} else if command == -1 {
			d = (d + 1) % 4
		} else {
			for i := 0; i < command; i++ {
				tx := x + dirs[d][0]
				ty := y + dirs[d][1]
				_, ok := obstaclesMap[[2]int{tx, ty}]
				if ok {
					break
				} else {
					x = tx
					y = ty
					res = max(res, tx*tx+ty*ty)
				}
			}
		}
	}
	return res
}
