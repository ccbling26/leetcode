package _86

type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	if head == nil {
		return head
	}
	big := &ListNode{0, nil}
	big_head := big
	small := &ListNode{0, nil}
	small_head := small
	for head != nil {
		if head.Val < x {
			small.Next = head
			small = small.Next
		} else {
			big.Next = head
			big = big.Next
		}
		head = head.Next
	}
	small.Next = big_head.Next
	big.Next = nil
	return small_head.Next
}
