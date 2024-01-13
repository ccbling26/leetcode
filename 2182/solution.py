class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        i, j, m = 25, 24, 0
        res = []
        while i >= 0 and j >= 0:
            if arr[i] == 0:
                m, i = 0, i - 1
            elif m < repeatLimit:
                arr[i] -= 1
                res.append(chr(ord('a') + i))
                m += 1
            elif j >= i or arr[j] == 0:
                j -= 1
            else:
                arr[j] -= 1
                res.append(chr(ord('a') + j))
                m = 0
        return "".join(res)
