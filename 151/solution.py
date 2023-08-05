from typing import List


class Solution:
    def reverse(self, s: List[str], i: int, j: int):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.reverse()
        x, y, l = 0, 0, 0
        while y < len(s):
            if s[y] != " ":
                x = y
                if l != 0:
                    s[l] = " "
                    l += 1
                while y < len(s) and s[y] != " ":
                    s[l] = s[y]
                    y += 1
                    l += 1
                self.reverse(s, l - y + x, l - 1)
            y += 1
        return "".join(s[:l])
