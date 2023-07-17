from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        dup = False
        val = -10 ** 4 - 1
        for i in range(len(nums)):
            if nums[i] == val and dup:
                continue
            elif nums[i] != val:
                dup = False
            else:
                dup = True
            nums[idx] = nums[i]
            val = nums[i]
            idx += 1
        return idx
