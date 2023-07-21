from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        obstacles = set([tuple(i) for i in obstacles])
        x, y, d, res = 0, 0, 0, 0
        for c in commands:
            if c < 0:
                d += 1 if c == -1 else -1
                d %= 4
            else:
                for i in range(c):
                    if (x + dirs[d][0], y + dirs[d][1]) in obstacles:
                        break
                    x, y = x + dirs[d][0], y + dirs[d][1]
                    res = max(res, x ** 2 + y ** 2)
        return res
