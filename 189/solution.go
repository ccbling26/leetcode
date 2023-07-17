package _189

func rotate(nums []int, k int) {
	var reverse func(l, h int)
	reverse = func(l, h int) {
		for l < h {
			nums[l], nums[h] = nums[h], nums[l]
			l++
			h--
		}
	}
	n := len(nums)
	k %= n
	reverse(0, n-1)
	reverse(0, k-1)
	reverse(k, n-1)
}
