class KMP:
    def __init__(self, pat: str):
        self.pat = pat
        m = len(pat)
        self.dp = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pat[i] != pat[j]:
                j = self.dp[j - 1]
            if pat[i] == pat[j]:
                j += 1
            self.dp[i] = j

    def search(self, txt: str):
        m = len(self.pat)
        n = len(txt)
        j = 0
        for i in range(n):
            while j > 0 and txt[i] != self.pat[j]:
                j = self.dp[j-1]
            if txt[i] == self.pat[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        kmp = KMP(needle)
        return kmp.search(haystack)
