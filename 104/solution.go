package _104

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Node struct {
	Val *TreeNode
	Nxt *Node
}

type Queue struct {
	Head   *Node
	Tail   *Node
	Length int
}

func (q *Queue) Append(node *TreeNode) {
	item := &Node{node, nil}
	if q.Head == nil {
		q.Head = item
		q.Tail = item
	} else {
		q.Tail.Nxt = item
		q.Tail = q.Tail.Nxt
	}
	q.Length++
}

func (q *Queue) PopLeft() *TreeNode {
	if q.Head == nil {
		return nil
	}
	res := q.Head.Val
	q.Head = q.Head.Nxt
	if q.Head == nil {
		q.Tail = nil
	}
	q.Length--
	return res
}

func (q *Queue) IsEmpty() bool {
	return q.Head == nil
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	q := Queue{}
	q.Append(root)
	for !q.IsEmpty() {
		length := q.Length
		for i := 0; i < length; i++ {
			node := q.PopLeft()
			if node.Left != nil {
				q.Append(node.Left)
			}
			if node.Right != nil {
				q.Append(node.Right)
			}
		}
		res++
	}
	return res
}
