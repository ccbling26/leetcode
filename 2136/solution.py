from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = list(zip(plantTime, growTime))
        arr.sort(key=lambda x: -x[1])
        res = 0
        cur = 0
        for p, g in arr:
            cur += p
            res = max(res, cur + g + 1)
        return res - 1
