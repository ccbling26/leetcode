from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i, num in enumerate(nums):
            val = target - num
            if num in tmp.keys():
                return [i, tmp[num]]
            else:
                tmp[val] = i
        return []
