package _143

type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	if head == nil {
		return
	}

	mid := findMiddle(head)
	l1 := head
	l2 := mid.Next
	mid.Next = nil
	l2 = reverse(l2)
	merge(l1, l2)
}

func findMiddle(head *ListNode) *ListNode {
	slow := head
	fast := head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow
}

func reverse(head *ListNode) *ListNode {
	var prev *ListNode
	cur := head
	for cur != nil {
		nxt := cur.Next
		cur.Next = prev
		prev = cur
		cur = nxt
	}
	return prev
}

func merge(l1 *ListNode, l2 *ListNode) {
	cur := l1
	for l2 != nil {
		tmp := l2
		l2 = l2.Next
		tmp.Next = cur.Next
		cur.Next = tmp
		cur = cur.Next.Next
	}
}
