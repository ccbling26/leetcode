import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        for i in range(n):
            dist[i] = math.ceil(dist[i] / speed[i])
        dist.sort()
        for i, item in enumerate(dist):
            if item <= i:
                return i
        return n
