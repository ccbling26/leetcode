package _722

func removeComments(source []string) []string {
	res := []string{}
	newLine := []byte{}
	isBlock := false
	for _, item := range source {
		i := 0
		n := len(item)
		for i < n {
			if isBlock {
				if i+1 < n && item[i] == '*' && item[i+1] == '/' {
					isBlock = false
					i++
				}
			} else {
				if i+1 < n && item[i] == '/' && item[i+1] == '*' {
					isBlock = true
					i++
				} else if i+1 < n && item[i] == '/' && item[i+1] == '/' {
					break
				} else {
					newLine = append(newLine, item[i])
				}
			}
			i++
		}
		if isBlock == false && len(newLine) > 0 {
			res = append(res, string(newLine))
			newLine = []byte{}
		}
	}
	return res
}
