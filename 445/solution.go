package _445

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	s1 := []int{}
	s2 := []int{}
	for l1 != nil {
		s1 = append(s1, l1.Val)
		l1 = l1.Next
	}
	for l2 != nil {
		s2 = append(s2, l2.Val)
		l2 = l2.Next
	}
	added := 0
	head := ListNode{-1, nil}
	for len(s1) != 0 || len(s2) != 0 {
		val := added
		if len(s1) != 0 {
			val += s1[len(s1)-1]
			s1 = s1[:len(s1)-1]
		}
		if len(s2) != 0 {
			val += s2[len(s2)-1]
			s2 = s2[:len(s2)-1]
		}
		tmp := ListNode{val % 10, head.Next}
		head.Next = &tmp
		added = val / 10
	}
	if added != 0 {
		return &ListNode{added, head.Next}
	}
	return head.Next
}
