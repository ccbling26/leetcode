from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_most = 0
        n = len(nums)
        for i in range(n):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
            else:
                return False
            if right_most >= n - 1:
                return True
        return True
