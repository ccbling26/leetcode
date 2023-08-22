package _48

func rotate(matrix [][]int) {
	n := len(matrix)
	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
	for i := 0; i < n; i++ {
		j, k := 0, n-1
		for j < k {
			matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
			j++
			k--
		}
	}
}
