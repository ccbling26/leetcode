package _83

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	l, r := head, head
	for r != nil {
		if l.Val != r.Val {
			l.Next = r
			l = r
		}
		r = r.Next
	}
	l.Next = nil
	return head
}
