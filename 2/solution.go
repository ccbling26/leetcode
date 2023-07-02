package _2

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	added := 0
	head := &ListNode{-1, nil}
	tmp := head
	for l1 != nil || l2 != nil {
		val := added
		if l1 != nil {
			val += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			val += l2.Val
			l2 = l2.Next
		}
		tmp.Next = &ListNode{val % 10, nil}
		tmp = tmp.Next
		added = val / 10
	}
	if added != 0 {
		tmp.Next = &ListNode{added, nil}
	}
	return head.Next
}
