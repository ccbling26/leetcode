class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, n = 0, len(columnTitle)
        base = 1
        for i in range(n - 1, -1, -1):
            val = ord(columnTitle[i]) - ord("A") + 1
            res += val * base
            base *= 26
        return res
