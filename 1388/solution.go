package _1388

func maxSizeSlices(slices []int) int {
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	cal := func(arr []int) int {
		m, n := len(arr), (len(arr)+1)/3
		dp := make([][]int, m)
		for i := 0; i < m; i++ {
			dp[i] = make([]int, n+1)
		}
		dp[0][1] = arr[0]
		dp[1][1] = max(arr[0], arr[1])
		for i := 2; i < m; i++ {
			for j := 1; j <= n; j++ {
				dp[i][j] = max(dp[i-2][j-1]+arr[i], dp[i-1][j])
			}
		}
		return dp[m-1][n]
	}
	ans := cal(slices[1:])
	ans = max(ans, cal(slices[:len(slices)-1]))
	return ans
}
