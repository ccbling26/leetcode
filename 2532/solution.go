package _2532

import "container/heap"

type waitItem struct{ totalTime, idx int }
type waitQueue []waitItem

func (w waitQueue) Len() int { return len(w) }
func (w waitQueue) Less(i, j int) bool {
	if w[i].totalTime == w[j].totalTime {
		return w[i].idx > w[j].idx
	} else {
		return w[i].totalTime > w[j].totalTime
	}
}
func (w waitQueue) Swap(i, j int)       { w[i], w[j] = w[j], w[i] }
func (w *waitQueue) Push(v interface{}) { *w = append(*w, v.(waitItem)) }
func (w *waitQueue) Pop() interface{} {
	n := len(*w)
	tmp := (*w)[n-1]
	*w = (*w)[:n-1]
	return tmp
}

type workItem struct{ finishTime, idx int }
type workQueue []workItem

func (w workQueue) Len() int            { return len(w) }
func (w workQueue) Less(i, j int) bool  { return w[i].finishTime < w[j].finishTime }
func (w workQueue) Swap(i, j int)       { w[i], w[j] = w[j], w[i] }
func (w *workQueue) Push(v interface{}) { *w = append(*w, v.(workItem)) }
func (w *workQueue) Pop() interface{} {
	n := len(*w)
	tmp := (*w)[n-1]
	*w = (*w)[:n-1]
	return tmp
}

func findCrossingTime(n int, k int, time [][]int) int {
	waitLeft := waitQueue{}
	waitRight := waitQueue{}
	workLeft := workQueue{}
	workRight := workQueue{}

	for idx, item := range time {
		heap.Push(&waitLeft, waitItem{item[0] + item[2], idx})
	}

	remain := n
	curTime := 0

	for {
		for len(workLeft) > 0 {
			if workLeft[0].finishTime > curTime {
				break
			}
			tmp := heap.Pop(&workLeft).(workItem)
			heap.Push(&waitLeft, waitItem{time[tmp.idx][0] + time[tmp.idx][2], tmp.idx})
		}
		for len(workRight) > 0 {
			if workRight[0].finishTime > curTime {
				break
			}
			tmp := heap.Pop(&workRight).(workItem)
			heap.Push(&waitRight, waitItem{time[tmp.idx][0] + time[tmp.idx][2], tmp.idx})
		}
		if len(waitRight) > 0 {
			tmp := heap.Pop(&waitRight).(waitItem)
			curTime += time[tmp.idx][2]
			heap.Push(&workLeft, workItem{curTime + time[tmp.idx][3], tmp.idx})
		} else if remain > 0 && len(waitLeft) > 0 {
			remain--
			tmp := heap.Pop(&waitLeft).(waitItem)
			curTime += time[tmp.idx][0]
			heap.Push(&workRight, workItem{curTime + time[tmp.idx][1], tmp.idx})
		} else {
			nextTime := 1 << 30
			if len(workLeft) > 0 {
				nextTime = min(nextTime, workLeft[0].finishTime)
			}
			if len(workRight) > 0 {
				nextTime = min(nextTime, workRight[0].finishTime)
			}
			if nextTime != 1<<30 {
				curTime = max(nextTime, curTime)
			}
		}
		if remain == 0 && len(waitRight) == 0 && len(workRight) == 0 {
			break
		}
	}
	return curTime
}

func min(a int, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
