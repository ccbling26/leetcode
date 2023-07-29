package _2569

type SegNode struct {
	l, r, total int64
	lazyTag     bool
}

type SegTree struct {
	nums []int
	arr  []SegNode
}

func (s *SegTree) Init(nums []int) {
	s.nums = nums
	n := len(nums)
	s.arr = make([]SegNode, 4*n+1)
	for i := 0; i < 4*n+1; i++ {
		s.arr[i] = SegNode{0, 0, 0, false}
	}
	s.Build(1, 0, int64(n-1))
}

func (s *SegTree) Build(idx, l, r int64) {
	obj := &s.arr[idx]
	obj.l = l
	obj.r = r
	if l == r {
		obj.total = int64(s.nums[l])
		return
	}
	mid := (l + r) / 2
	s.Build(2*idx, l, mid)
	s.Build(2*idx+1, mid+1, r)
	obj.total = s.arr[2*idx].total + s.arr[2*idx+1].total
}

func (s *SegTree) ReverseRange(l, r int64) {
	s.Modify(1, l, r)
}

func (s *SegTree) SumRange(l, r int64) int64 {
	return s.Query(1, l, r)
}

func (s *SegTree) Modify(idx, l, r int64) {
	obj := &s.arr[idx]
	if obj.l >= l && obj.r <= r {
		obj.lazyTag = !obj.lazyTag
		obj.total = obj.r - obj.l + 1 - obj.total
		return
	}
	s.PushDown(idx)
	if s.arr[2*idx].r >= l {
		s.Modify(2*idx, l, r)
	}
	if s.arr[2*idx+1].l <= r {
		s.Modify(2*idx+1, l, r)
	}
	obj.total = s.arr[2*idx].total + s.arr[2*idx+1].total
}

func (s *SegTree) PushDown(idx int64) {
	if s.arr[idx].lazyTag == true {
		s.arr[2*idx].lazyTag = !s.arr[2*idx].lazyTag
		s.arr[2*idx].total = s.arr[2*idx].r - s.arr[2*idx].l + 1 - s.arr[2*idx].total
		s.arr[2*idx+1].lazyTag = !s.arr[2*idx+1].lazyTag
		s.arr[2*idx+1].total = s.arr[2*idx+1].r - s.arr[2*idx+1].l + 1 - s.arr[2*idx+1].total
		s.arr[idx].lazyTag = false
	}
}
func (s *SegTree) Query(idx, l, r int64) int64 {
	obj := &s.arr[idx]
	if obj.r < l || obj.l > r {
		return 0
	}
	if obj.l >= l && obj.r <= r {
		return obj.total
	}
	s.PushDown(idx)
	res := int64(0)
	if s.arr[2*idx].r >= l {
		res += s.Query(2*idx, l, r)
	}
	if s.arr[2*idx].l <= r {
		res += s.Query(2*idx+1, l, r)
	}
	return res
}

func handleQuery(nums1 []int, nums2 []int, queries [][]int) []int64 {
	tree := new(SegTree)
	tree.Init(nums1)
	ans := []int64{}
	n, total := len(nums1), int64(0)
	for _, val := range nums2 {
		total += int64(val)
	}
	for _, query := range queries {
		x, y, z := query[0], int64(query[1]), int64(query[2])
		if x == 1 {
			tree.ReverseRange(y, z)
		} else if x == 2 {
			total += tree.SumRange(0, int64(n-1)) * y
		} else {
			ans = append(ans, total)
		}
	}
	return ans
}
