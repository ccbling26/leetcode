package _135

func candy(ratings []int) int {
	n := len(ratings)
	res := 1
	inc, dec, pre := 1, 0, 1
	for i := 1; i < n; i++ {
		if ratings[i] >= ratings[i-1] {
			dec = 0
			if ratings[i] == ratings[i-1] {
				pre = 1
			} else {
				pre++
			}
			res += pre
			inc = pre
		} else {
			dec++
			if dec == inc {
				dec++
			}
			res += dec
			pre = 1
		}
	}
	return res
}
