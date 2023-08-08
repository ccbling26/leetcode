from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        a, b = 0, 0
        for i in range(n):
            a = max(a, nums[i])
            b = min(b, nums[i])
        return a - b