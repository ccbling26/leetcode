from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        q = []
        res = [0] * n
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while q and q[-1] < h:
                res[i] += 1
                q.pop()
            if q:
                res[i] += 1
            q.append(h)
        return res
