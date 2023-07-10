import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = sys.maxsize
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if abs(tmp - target) < abs(res - target):
                    res = tmp
                if tmp == target:
                    return tmp
                elif tmp < target:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                else:
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
        return res
