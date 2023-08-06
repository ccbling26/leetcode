package _24

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	res := &ListNode{-1, head}
	pre := res
	n1 := res.Next
	n2 := n1.Next
	for n1 != nil && n2 != nil {
		pre.Next = n2
		n1.Next = n2.Next
		n2.Next = n1
		pre = n1
		n1 = pre.Next
		if n1 == nil {
			break
		}
		n2 = n1.Next
	}
	return res.Next
}
