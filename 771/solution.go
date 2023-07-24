package _771

func numJewelsInStones(jewels string, stones string) int {
	dict := map[rune]bool{}
	for _, c := range jewels {
		dict[c] = true
	}
	res := 0
	for _, c := range stones {
		_, ok := dict[c]
		if ok == true {
			res++
		}
	}
	return res
}
