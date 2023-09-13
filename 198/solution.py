from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b, c = 0, 0, 0
        for item in nums:
            v = max(a, b) + item
            a, b, c = b, c, v
        return max(a, b, c)
