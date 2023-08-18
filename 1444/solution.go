package _1444

import "math"

func ways(pizza []string, k int) int {
	rows, cols := len(pizza), len(pizza[0])
	mod := int(math.Pow(10, 9)) + 7
	dp := make([][]int, rows+1)
	for i := 0; i <= rows; i++ {
		dp[i] = make([]int, cols+1)
	}
	ans := make([][][]int, k)
	for i := 0; i < k; i++ {
		ans[i] = make([][]int, rows)
		for j := 0; j < rows; j++ {
			ans[i][j] = make([]int, cols)
		}
	}
	for i := rows - 1; i >= 0; i-- {
		for j := cols - 1; j >= 0; j-- {
			dp[i][j] = dp[i+1][j] + dp[i][j+1] - dp[i+1][j+1]
			if pizza[i][j] == 'A' {
				dp[i][j]++
			}
			if dp[i][j] > 0 {
				ans[0][i][j] = 1
			}
		}
	}
	for a := 1; a < k; a++ {
		for b := 0; b < rows; b++ {
			for c := 0; c < cols; c++ {
				for d := b + 1; d < rows; d++ {
					if dp[b][c] == dp[d][c] {
						continue
					} else if dp[d][c] == 0 {
						break
					} else {
						ans[a][b][c] = (ans[a][b][c] + ans[a-1][d][c]) % mod
					}
				}
				for d := c + 1; d < cols; d++ {
					if dp[b][c] == dp[b][d] {
						continue
					} else if dp[b][d] == 0 {
						break
					} else {
						ans[a][b][c] = (ans[a][b][c] + ans[a-1][b][d]) % mod
					}
				}
			}
		}
	}
	return ans[k-1][0][0]
}
