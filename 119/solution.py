from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        pre = [1, 1]
        for i in range(2, rowIndex + 1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(pre[j] + pre[j - 1])
            tmp.append(1)
            pre = tmp
        return pre
