package _1851

import (
	"container/heap"
	"sort"
)

type IntervalHeap [][]int

func (h IntervalHeap) Len() int           { return len(h) }
func (h IntervalHeap) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h IntervalHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntervalHeap) Push(x interface{}) {
	*h = append(*h, x.([]int))
}
func (h *IntervalHeap) Pop() interface{} {
	old := *h
	n := len(old)
	res := old[n-1]
	*h = old[:n-1]
	return res
}

func minInterval(intervals [][]int, queries []int) []int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	sortedQueries := make([][2]int, len(queries))
	for i, query := range queries {
		sortedQueries[i] = [2]int{query, i}
	}
	sort.Slice(sortedQueries, func(i, j int) bool {
		return sortedQueries[i][0] < sortedQueries[j][0]
	})
	intervalHeap := &IntervalHeap{}
	heap.Init(intervalHeap)
	res := make([]int, len(queries))

	i := 0
	for _, query := range sortedQueries {
		val, idx := query[0], query[1]
		for i < len(intervals) && intervals[i][0] <= val {
			begin, end := intervals[i][0], intervals[i][1]
			length := end - begin + 1
			heap.Push(intervalHeap, []int{length, end})
			i++
		}
		for intervalHeap.Len() > 0 && (*intervalHeap)[0][1] < val {
			heap.Pop(intervalHeap)
		}
		if intervalHeap.Len() > 0 {
			res[idx] = (*intervalHeap)[0][0]
		} else {
			res[idx] = -1
		}
	}
	return res
}
