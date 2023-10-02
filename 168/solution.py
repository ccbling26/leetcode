class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber, tmp = columnNumber // 26, columnNumber % 26
            if tmp == 0:
                tmp = 25
                columnNumber -= 1
            else:
                tmp -= 1
            res.append(chr(ord("A") + tmp))
        res.reverse()
        return "".join(res)
