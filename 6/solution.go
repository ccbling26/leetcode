package _6

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	arr := make([][]rune, numRows)
	cur, flag := 0, -1
	for _, c := range s {
		arr[cur] = append(arr[cur], c)
		if cur == 0 || cur == numRows-1 {
			flag *= -1
		}
		cur += flag
	}
	res := []rune{}
	for _, item := range arr {
		res = append(res, item...)
	}
	return string(res)
}
