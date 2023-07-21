package _1499

import "math"

func findMaxValueOfEquation(points [][]int, k int) int {
	res := math.MinInt
	q := [][]int{}
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	for _, point := range points {
		x, y := point[0], point[1]
		for len(q) > 0 && x-q[0][1] > k {
			q = q[1:]
		}
		if len(q) > 0 {
			res = max(res, x+y+q[0][0])
		}
		for len(q) > 0 && y-x >= q[len(q)-1][0] {
			q = q[:len(q)-1]
		}
		q = append(q, []int{y - x, x})
	}
	return res
}
