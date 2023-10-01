from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            if i == 1:
                res.append([1, 1])
            else:
                tmp = [1]
                n = len(res[i - 1])
                for j in range(1, n):
                    tmp.append(res[i - 1][j] + res[i - 1][j - 1])
                tmp.append(1)
                res.append(tmp)
        return res
