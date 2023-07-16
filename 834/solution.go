package _834

func sumOfDistancesInTree(n int, edges [][]int) []int {
	edgeDict := make([][]int, n)
	for _, edge := range edges {
		x, y := edge[0], edge[1]
		edgeDict[x] = append(edgeDict[x], y)
		edgeDict[y] = append(edgeDict[y], x)
	}

	dp := make([]int, n)
	sz := make([]int, n)

	var dfs1 func(child, father int)
	dfs1 = func(child, father int) {
		sz[child] = 1
		for _, item := range edgeDict[child] {
			if item == father {
				continue
			}
			dfs1(item, child)
			dp[child] += dp[item] + sz[item]
			sz[child] += sz[item]
		}
	}

	dfs1(0, -1)

	res := make([]int, n)

	var dfs2 func(child, father int)
	dfs2 = func(child, father int) {
		res[child] = dp[child]

		for _, item := range edgeDict[child] {
			if item == father {
				continue
			}

			pu, pv := dp[child], dp[item]
			su, sv := sz[child], sz[item]

			dp[child] -= dp[item] + sz[item]
			sz[child] -= sz[item]
			dp[item] += dp[child] + sz[child]
			sz[item] += sz[child]

			dfs2(item, child)

			dp[child], dp[item] = pu, pv
			sz[child], sz[item] = su, sv
		}
	}

	dfs2(0, -1)

	return res
}
