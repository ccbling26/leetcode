from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        def _rob(i, j):
            a, b, c = 0, 0, nums[i]
            for k in range(i + 1, j):
                a, b, c = b, c, max(a, b) + nums[k]
            return max(b, c)

        return max(_rob(0, n - 1), _rob(1, n))
