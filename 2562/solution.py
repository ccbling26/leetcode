from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range((n + 1) // 2):
            val1 = nums[i]
            val2 = nums[n - 1 - i]
            if i == n - 1 - i:
                res += val1
            else:
                res += int(str(val1) + str(val2))
        return res
