from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res, firstIdx = -1, 0
        for i in range(1, len(nums)):
            length = i - firstIdx + 1
            if nums[i] - nums[firstIdx] == (length - 1) % 2:
                res = max(res, length)
            elif nums[i] - nums[i - 1] == 1:
                firstIdx = i - 1
                res = max(res, 2)
            else:
                firstIdx = i
        return res
