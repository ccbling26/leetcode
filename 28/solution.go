package _28

type KMP struct {
	pattern string
	dp      []int
}

func (k *KMP) Init(pattern string) {
	k.pattern = pattern
	m := len(pattern)
	k.dp = make([]int, m)
	j := 0
	for i := 1; i < m; i++ {
		for j > 0 && pattern[i] != pattern[j] {
			j = k.dp[j-1]
		}
		if pattern[i] == pattern[j] {
			j++
		}
		k.dp[i] = j
	}
}

func (k KMP) Search(txt string) int {
	j, m := 0, len(k.pattern)
	for i := 0; i < len(txt); i++ {
		for j > 0 && txt[i] != k.pattern[j] {
			j = k.dp[j-1]
		}
		if txt[i] == k.pattern[j] {
			j++
		}
		if j == m {
			return i - m + 1
		}
	}
	return -1
}

func strStr(haystack string, needle string) int {
	k := new(KMP)
	k.Init(needle)
	return k.Search(haystack)
}
