from bisect import bisect_left
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def f(y : int) -> int:
            count, visited = 0, False
            for x in nums:
                if x <= y and not visited:
                    count, visited = count + 1, True
                else:
                    visited = False
            return count
        return bisect_left(range(min(nums), max(nums)), k, key = f) + min(nums)
