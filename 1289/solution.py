import sys
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = [0, -1, 0]
        tmp = [sys.maxsize, -1, sys.maxsize]
        for i in range(n):
            for j in range(m):
                grid[i][j] += res[0] if j != res[1] else res[2]
                if grid[i][j] <= tmp[0]:
                    tmp[2] = tmp[0]
                    tmp[1] = j
                    tmp[0] = grid[i][j]
                elif grid[i][j] <= tmp[2]:
                    tmp[2] = grid[i][j]
            res = tmp
            tmp = [sys.maxsize, -1, sys.maxsize]
        return res[0]
