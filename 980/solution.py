from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sj, sj, st = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    si, sj = i, j
                elif grid[i][j] in [0, 2]:
                    st |= 1 << (n * i + j)

        @lru_cache(None)
        def find(x: int, y: int, z: int) -> int:
            if grid[x][y] == 2:
                if z == 0:
                    return 1
                return 0
            cases = ((1, 0), (-1, 0), (0, 1), (0, -1))
            res = 0
            for i, j in cases:
                ti, tj = x + i, y + j
                if 0 <= ti < m and 0 <= tj < n and (z & 1 << (n * ti + tj)):
                    res += find(ti, tj, z ^ (1 << (n * ti + tj)))
            return res

        return find(si, sj, st)
