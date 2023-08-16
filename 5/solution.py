class Solution:
    def find(self, i: int, j: int):
        while (i >= 0 and j < self.n):
            if self.s[i] != self.s[j]:
                break
            i -= 1
            j += 1
        if j - i - 1 > self.length:
            self.length = j - i - 1
            self.begin = i + 1
            self.end = j - 1

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.n = len(s)
        self.length = 1
        self.begin = 0
        self.end = 0
        for i in range(self.n):
            self.find(i, i)
            self.find(i, i + 1)
        return s[self.begin:self.end + 1]
