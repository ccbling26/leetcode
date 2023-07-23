from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = nums[0]
        for i in range(1, n):
            res[i] = nums[i] * res[i - 1]
        for i in range(n - 2, -1, -1):
            nums[i] *= nums[i + 1]
        res[n - 1] = res[n - 2]
        for i in range(n - 2, 0, -1):
            res[i] = res[i - 1] * nums[i + 1]
        res[0] = nums[1]
        return res
