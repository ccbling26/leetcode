from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        val = -10 ** 4
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                val = nums[i]
                idx += 1
        return idx
