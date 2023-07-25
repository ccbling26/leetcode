package _125

func isPalindrome(s string) bool {
	i := 0
	j := len(s) - 1
	for i < j {
		for i < j && !isalnum(s[i]) {
			i++
		}
		for i < j && !isalnum(s[j]) {
			j--
		}
		if i < j {
			if to_lower(s[i]) != to_lower(s[j]) {
				return false
			}
			i++
			j--
		}
	}
	return true
}

func to_lower(ch byte) byte {
	if ch >= 'A' && ch <= 'Z' {
		return ch - 'A' + 'a'
	}
	return ch
}

func isalnum(ch byte) bool {
	return (ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9')
}
