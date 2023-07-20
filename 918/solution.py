from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        preMax, maxRes = nums[0], nums[0]
        preMin, minRes = nums[0], nums[0]
        total = nums[0]
        for i in range(1, n):
            preMax = max(preMax + nums[i], nums[i])
            maxRes = max(maxRes, preMax)
            preMin = min(preMin + nums[i], nums[i])
            minRes = min(minRes, preMin)
            total += nums[i]
        if maxRes < 0:
            return maxRes
        else:
            return max(maxRes, total - minRes)