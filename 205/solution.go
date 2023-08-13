package _205

func isIsomorphic(s string, t string) bool {
	relations1 := map[byte]byte{}
	relations2 := map[byte]byte{}
	n := len(s)
	for i := 0; i < n; i++ {
		x := s[i]
		y := t[i]
		val1, ok1 := relations1[x]
		val2, ok2 := relations2[y]
		if ok1 {
			if val1 != y {
				return false
			}
		} else if ok2 {
			if val2 != x {
				return false
			}
		} else {
			relations1[x] = y
			relations2[y] = x
		}
	}
	return true
}
