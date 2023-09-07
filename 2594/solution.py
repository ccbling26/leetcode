import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, ranks[0] * cars * cars

        def check(t: int) -> bool:
            return sum(math.floor(math.sqrt(t / rank)) for rank in ranks) >= cars
 
        while l < r:
            mid = math.floor((l + r) / 2)
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
