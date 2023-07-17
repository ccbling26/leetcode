class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        add = 0
        res = []
        while i >= 0 or j >= 0:
            val1 = int(num1[i]) if i >= 0 else 0
            val2 = int(num2[j]) if j >= 0 else 0
            total = add + val1 + val2
            res.append(str(total % 10))
            add = total // 10
            i -= 1
            j -= 1
        if add > 0:
            res.append(str(add))
        res.reverse()
        return "".join(res)
