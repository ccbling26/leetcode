from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda p: (p[0], -p[1]))
        heights = [item[1] for item in envelopes]
        res = []
        n = 0
        for item in heights:
            i = bisect_left(res, item)
            if i >= n:
                res.append(item)
                n += 1
            else:
                res[i] = item
        return n
