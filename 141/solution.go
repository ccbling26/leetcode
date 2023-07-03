package _141

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	p1 := head
	p2 := head.Next
	for p1 != p2 && p2.Next != nil && p2.Next.Next != nil {
		p1 = p1.Next
		p2 = p2.Next.Next
	}
	return p1 == p2
}
