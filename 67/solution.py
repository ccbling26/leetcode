class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        added = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                added += int(a[i])
                i -= 1
            if j >= 0:
                added += int(b[j])
                j -= 1
            res = str(added % 2) + res
            added //= 2
        if added:
            return "1" + res
        return res
