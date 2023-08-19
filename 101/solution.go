package _101

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type QueueItem struct {
	Val *TreeNode
	Nxt *QueueItem
}

type Queue struct {
	Head *QueueItem
	Tail *QueueItem
}

func (q *Queue) append(node *TreeNode) {
	item := &QueueItem{node, nil}
	if q.Head == nil {
		q.Head = item
		q.Tail = item
	} else {
		q.Tail.Nxt = item
		q.Tail = q.Tail.Nxt
	}
}

func (q *Queue) popLeft() *TreeNode {
	if q.IsEmpty() {
		return nil
	}
	res := q.Head.Val
	q.Head = q.Head.Nxt
	if q.Head == nil {
		q.Tail = nil
	}
	return res
}

func (q *Queue) IsEmpty() bool {
	return q.Head == nil
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	queue := Queue{}
	queue.append(root.Left)
	queue.append(root.Right)
	for !queue.IsEmpty() {
		left := queue.popLeft()
		right := queue.popLeft()
		if left != nil && right == nil || left == nil && right != nil {
			return false
		} else if left == nil && right == nil {
			continue
		} else if left.Val != right.Val {
			return false
		} else {
			queue.append(left.Left)
			queue.append(right.Right)
			queue.append(left.Right)
			queue.append(right.Left)
		}
	}
	return true
}
