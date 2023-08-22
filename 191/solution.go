package _191

func hammingWeight(num uint32) int {
	res := 0
	for num != 0 {
		if num&1 != 0 {
			res++
		}
		num >>= 1
	}
	return res
}
