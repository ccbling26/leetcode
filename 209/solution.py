from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        i = j = 0
        total = 0
        while j < n:
            total += nums[j]
            j += 1
            while total >= target:
                res = min(res, j - i)
                total -= nums[i]
                i += 1
        return 0 if res == (n + 1) else res
