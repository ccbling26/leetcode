package _35

func searchInsert(nums []int, target int) int {
	var find func(l, r int) int
	find = func(l, r int) int {
		if l > r {
			return l
		}
		mid := (l + r) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			return find(l, mid-1)
		} else {
			return find(mid+1, r)
		}
	}
	return find(0, len(nums)-1)
}
