package _383

func canConstruct(ransomNote string, magazine string) bool {
	counter := map[rune]int{}
	for _, c := range magazine {
		counter[c]++
	}
	for _, c := range ransomNote {
		val, ok := counter[c]
		if ok == false || val == 0 {
			return false
		}
		counter[c]--
	}
	return true
}
