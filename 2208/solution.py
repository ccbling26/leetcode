from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        n, total = len(nums), 0
        for i in range(n):
            total += nums[i]
            nums[i] *= -1
        count = 0
        res = 0
        heapify(nums)
        while count < total / 2:
            num = heappop(nums)
            num /= 2
            count -= num
            res += 1
            heappush(nums, num)
        return res
