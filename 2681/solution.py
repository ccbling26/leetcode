from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        res, dp, pre_sum = 0, 0, 0
        for i in range(n):
            dp = (nums[i] + pre_sum) % mod
            pre_sum = (pre_sum + dp) % mod
            res = (res + dp * nums[i] * nums[i]) % mod
        return res
