from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        for i in range(m):
            grid[i].sort()
        n = len(grid[0])
        res = 0
        for i in range(n):
            tmp = grid[0][i]
            for j in range(1, m):
                tmp = max(tmp, grid[j][i])
            res += tmp
        return res
