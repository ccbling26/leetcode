from heapq import heapify, heappop, heappush
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        res = 0
        for _ in range(k):
            num = heappop(nums)
            res -= num
            heappush(nums, -math.ceil(-num / 3))
        return res
