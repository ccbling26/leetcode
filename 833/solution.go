package _833

import "strings"

type replaceItem struct {
	item string
	len  int
}

func findReplaceString(s string, indices []int, sources []string, targets []string) string {
	replace := make([]replaceItem, len(s))
	for idx, c := range s {
		replace[idx] = replaceItem{string(c), 1}
	}
	n := len(indices)
	isStartsWith := func(source string, indice int) bool {
		for i := 0; i < len(source); i++ {
			if indice >= len(s) {
				return false
			}
			if s[indice] != source[i] {
				return false
			}
			indice++
		}
		return true
	}
	for i := 0; i < n; i++ {
		if isStartsWith(sources[i], indices[i]) {
			replace[indices[i]] = replaceItem{targets[i], len(sources[i])}
		}
	}
	ans := []string{}
	i := 0
	for i < len(replace) {
		ans = append(ans, replace[i].item)
		i += replace[i].len
	}
	return strings.Join(ans, "")
}
