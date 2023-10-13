from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        pools = {}
        drop = SortedList()
        n = len(rains)
        res = [1] * n
        for i in range(n):
            rain = rains[i]
            if rain == 0:
                drop.add(i)
            else:
                res[i] = -1
                if rain in pools:
                    j = pools[rain]
                    k = drop.bisect(j)
                    if k == len(drop):
                        return []
                    else:
                        res[drop[k]] = rain
                        drop.discard(drop[k])
                pools[rain] = i
        return res
