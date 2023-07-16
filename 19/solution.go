package _19

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	p1 := head
	for i := 0; i < n; i++ {
		p1 = p1.Next
	}
	if p1 == nil {
		return head.Next
	}
	p2 := head
	for p1.Next != nil {
		p1 = p1.Next
		p2 = p2.Next
	}
	delNode := p2.Next
	p2.Next = delNode.Next
	return head
}
