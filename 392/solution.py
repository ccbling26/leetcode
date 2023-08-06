class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, l1, l2 = 0, 0, len(s), len(t)
        while i < l1 and j < l2:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == l1
