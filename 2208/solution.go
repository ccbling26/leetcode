package _2208

import "container/heap"

type FloatHeap []float64

func (h FloatHeap) Len() int           { return len(h) }
func (h FloatHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h FloatHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *FloatHeap) Push(x interface{}) {
	*h = append(*h, x.(float64))
}
func (h *FloatHeap) Pop() interface{} {
	old := *h
	n := old.Len()
	res := old[n-1]
	*h = old[:n-1]
	return res
}

func halveArray(nums []int) int {
	total := 0.0
	h := &FloatHeap{}
	heap.Init(h)
	for _, num := range nums {
		total += float64(num)
		heap.Push(h, float64(num))
	}
	count := 0.0
	res := 0
	for count < total/2 {
		num := (heap.Pop(h)).(float64)
		num /= 2
		heap.Push(h, num)
		count += num
		res++
	}
	return res
}
