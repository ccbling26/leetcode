package _92

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	tmp1 := &ListNode{0, head}
	tmp2 := tmp1
	for i := 1; i < left; i++ {
		tmp2 = tmp2.Next
	}
	cur := tmp2.Next
	var pre, nxt *ListNode
	for i := 0; i <= right-left; i++ {
		nxt = cur.Next
		cur.Next = pre
		pre = cur
		cur = nxt
	}
	tmp2.Next = pre
	for tmp2.Next != nil {
		tmp2 = tmp2.Next
	}
	tmp2.Next = nxt
	return tmp1.Next
}
