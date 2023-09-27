from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        for i, r, v, p, d in restaurants:
            if v >= veganFriendly and p <= maxPrice and d <= maxDistance:
                res.append((i, r))
        n = len(res)
        res.sort(key=lambda p: (-p[1], -p[0]))
        for i in range(n):
            res[i] = res[i][0]
        return res
