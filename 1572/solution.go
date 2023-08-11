package _1572

func diagonalSum(mat [][]int) int {
	n := len(mat)
	res := 0
	for i := 0; i < n; i++ {
		res += mat[i][i] + mat[i][n - i - 1]
	}
	if n % 2 == 1 {
		res -= mat[n / 2][n / 2]
	}
	return res
}