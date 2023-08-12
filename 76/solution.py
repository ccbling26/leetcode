class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if n < len(t):
            return ""
        counter = {}
        count = 0
        for c in t:
            if c not in counter:
                count += 1
                counter[c] = 1
            else:
                counter[c] += 1
        i, j, p, q = 0, 0, 0, n
        while j < n:
            c = s[j]
            j += 1
            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    count -= 1
            while i < j and count == 0:
                if q - p + 1 > j - i:
                    p = i
                    q = j - 1
                c = s[i]
                i += 1
                if c in counter:
                    if counter[c] == 0:
                        count += 1
                    counter[c] += 1
        if q == n:
            return ""
        else:
            return s[p:q+1]
