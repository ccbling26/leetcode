package _68

import "strings"

func fullJustify(words []string, maxWidth int) []string {
	res := []string{}
	i := 0
	n := len(words)
	for i < n {
		left := i
		l := 0
		for i < n && l+len(words[i])+i-left <= maxWidth {
			l += len(words[i])
			i++
		}
		black_count := maxWidth - l
		if i == n {
			res = append(res, strings.Join(words[left:], " ")+strings.Repeat(" ", black_count-i+left+1))
			break
		}
		count := i - left
		if count == 1 {
			res = append(res, words[left]+strings.Repeat(" ", black_count))
		} else {
			item := ""
			avg := black_count / (count - 1)
			more := black_count % (count - 1)
			for j := 0; j < more; j++ {
				item += words[left+j] + strings.Repeat(" ", avg+1)
			}
			res = append(res, item+strings.Join(words[left+more:i], strings.Repeat(" ", avg)))
		}
	}
	return res
}
