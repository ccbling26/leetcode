from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        a, b, c, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while a <= b and c <= d:
            for i in range(a, b + 1):
                res.append(matrix[c][i])
            c += 1
            for i in range(c, d + 1):
                res.append(matrix[i][b])
            b -= 1
            if a > b or c > d:
                break
            for i in range(b, a - 1, -1):
                res.append(matrix[d][i])
            d -= 1
            for i in range(d, c - 1, -1):
                res.append(matrix[i][a])
            a += 1
        return res
