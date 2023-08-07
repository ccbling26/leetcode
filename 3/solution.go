package _3

func lengthOfLongestSubstring(s string) int {
	dict := map[byte]struct{}{}
	n, i, j, res := len(s), 0, 0, 0
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	for j < n {
		c := s[j]
		for i < j {
			_, ok := dict[c]
			if !ok {
				break
			}
			delete(dict, s[i])
			i++
		}
		dict[c] = struct{}{}
		j++
		res = max(res, j-i)
	}
	return res
}
