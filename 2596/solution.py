from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if not n:
            return True
        m = len(grid[0])
        if not m:
            return True
        if grid[0][0] != 0:
            return False
        x, y = 0, 0
        nxt = 1
        flag = True
        arr = (
            (1, 2), (1, -2), (2, 1), (2, -1),
            (-1, 2), (-1, -2), (-2, 1), (-2, -1)
        )
        while flag:
            if nxt == n * m:
                return True
            flag = False
            for a, b in arr:
                cur_x, cur_y = x + a, y + b
                if 0 <= cur_x < n and 0 <= cur_y < m and grid[cur_x][cur_y] == nxt:
                    nxt += 1
                    flag = True
                    x, y = cur_x, cur_y
                    break
        return False
