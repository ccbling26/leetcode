package _931

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func minFallingPathSum(matrix [][]int) int {
	n := len(matrix)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	copy(dp[0], matrix[0])
	for i := 1; i < n; i++ {
		for j := 0; j < n; j++ {
			tmp := dp[i-1][j]
			if j > 0 {
				tmp = min(tmp, dp[i-1][j-1])
			}
			if j < n-1 {
				tmp = min(tmp, dp[i-1][j+1])
			}
			dp[i][j] = matrix[i][j] + tmp
		}
	}
	res := dp[n-1][0]
	for i := 1; i < n; i++ {
		res = min(res, dp[n-1][i])
	}
	return res
}
