from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        mapping = {}
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                mapping[mat[i][j]] = i * n + j
        rows = [n] * m
        cols = [m] * n
        for i, val in enumerate(arr):
            index = mapping[val]
            row = index // n
            col = index % n
            rows[row] -= 1
            cols[col] -= 1
            if rows[row] == 0 or cols[col] == 0:
                return i
        return -1
