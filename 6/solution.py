class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = ["" for i in range(numRows)]
        cur, flag = 0, -1
        for i in range(len(s)):
            arr[cur] += s[i]
            if cur == 0 or cur == numRows - 1:
                flag *= -1
            cur += flag
        return "".join(arr)
