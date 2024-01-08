from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for x1, y1 in points:
            dists = defaultdict(int)
            for x2, y2 in points:
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dists[dist] += 1
            for cnt in dists.values():
                res += (cnt - 1) * cnt
        return res
