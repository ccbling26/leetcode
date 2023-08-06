package _11

func maxArea(height []int) int {
	i, j := 0, len(height)-1
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	res := 0
	for i < j {
		if height[i] < height[j] {
			res = max(res, (j-i)*height[i])
			i++
		} else {
			res = max(res, (j-i)*height[j])
			j--
		}
	}
	return res
}
