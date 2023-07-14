package _979

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var res int

func distributeCoins(root *TreeNode) int {
	res = 0
	dfs(root)
	return res
}

func abs(val int) int {
	if val < 0 {
		return -val
	}
	return val
}

func dfs(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := dfs(root.Left)
	right := dfs(root.Right)
	res += abs(left) + abs(right)
	return left + right + root.Val - 1
}
