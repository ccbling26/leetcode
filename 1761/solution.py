from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        res = 3 * n
        arcs = [[0] * (n + 1) for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            arcs[x][y] = 1
            arcs[y][x] = 1
            arcs[x][n] += 1
            arcs[y][n] += 1
        for i in range(n):
            for j in range(i + 1, n):
                if arcs[i][j] != 1:
                    continue
                for k in range(j + 1, n):
                    if arcs[i][k] != 1 or arcs[j][k] != 1:
                        continue
                    res = min(res, arcs[i][n] + arcs[j][n] + arcs[k][n] - 6)
        return -1 if res == 3 * n else res
