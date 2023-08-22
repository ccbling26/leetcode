from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i, j = -1, 0
        res, n = 0, len(seats)
        while j < n:
            while j < n and seats[j] == 0:
                j += 1
            if i == -1:
                res = j
            elif j >= n:
                res = max(res, j - i - 1)
            else:
                res = max(res, (j - i) // 2)
            i = j
            j += 1
        return res
