package _23

type ListNode struct {
	Val  int
	Next *ListNode
}

type Heap struct {
	Arr    []*ListNode
	Length int
}

func (h *Heap) push(obj *ListNode) {
	h.Length++
	h.Arr[h.Length] = obj
	h.up(h.Length)
}

func (h *Heap) pop() *ListNode {
	res := h.Arr[1]
	h.Arr[1], h.Arr[h.Length] = h.Arr[h.Length], h.Arr[1]
	h.Length--
	h.down(1)
	return res
}

func (h *Heap) up(idx int) {
	if idx == 1 {
		return
	}
	father_idx := idx / 2
	if h.Arr[idx].Val < h.Arr[father_idx].Val {
		h.Arr[idx], h.Arr[father_idx] = h.Arr[father_idx], h.Arr[idx]
		h.up(father_idx)
	}
}

func (h *Heap) down(idx int) {
	left_idx := idx * 2
	if left_idx <= h.Length && h.Arr[left_idx].Val < h.Arr[idx].Val {
		h.Arr[idx], h.Arr[left_idx] = h.Arr[left_idx], h.Arr[idx]
		h.down(left_idx)
	}
	right_idx := idx*2 + 1
	if right_idx <= h.Length && h.Arr[right_idx].Val < h.Arr[idx].Val {
		h.Arr[idx], h.Arr[right_idx] = h.Arr[right_idx], h.Arr[idx]
		h.down(right_idx)
	}
}

func mergeKLists(lists []*ListNode) *ListNode {
	n := len(lists)
	heap := Heap{make([]*ListNode, n+1), 0}
	for _, item := range lists {
		if item != nil {
			heap.push(item)
		}
	}
	head := &ListNode{-1, nil}
	cur := head
	for heap.Length != 0 {
		tmp := heap.pop()
		cur.Next = tmp
		cur = cur.Next
		if tmp.Next != nil {
			heap.push(tmp.Next)
		}
	}
	return head.Next
}
