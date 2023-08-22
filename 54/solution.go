package _54

func spiralOrder(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	a, b, c, d := 0, n-1, 0, m-1
	res := []int{}
	for a <= b && c <= d {
		for i := a; i <= b; i++ {
			res = append(res, matrix[c][i])
		}
		c++
		for i := c; i <= d; i++ {
			res = append(res, matrix[i][b])
		}
		b--
		if a > b || c > d {
			break
		}
		for i := b; i >= a; i-- {
			res = append(res, matrix[d][i])
		}
		d--
		for i := d; i >= c; i-- {
			res = append(res, matrix[i][a])
		}
		a++
	}
	return res
}
