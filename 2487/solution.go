package _2487

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNodes(head *ListNode) *ListNode {
	var pre, nxt *ListNode
	cur := head
	for cur != nil {
		nxt = cur.Next
		cur.Next = pre
		pre = cur
		cur = nxt
		for pre.Next != nil && pre.Val > pre.Next.Val {
			pre.Next = pre.Next.Next
		}
	}
	cur = pre
	pre = nil
	for cur != nil {
		nxt = cur.Next
		cur.Next = pre
		pre = cur
		cur = nxt
	}
	return pre
}
