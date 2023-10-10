from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod, n = 10 ** 9 + 7, len(nums)
        for i in range(n):
            nums[i] += d * (1 if s[i] == 'R' else -1)
        nums.sort()
        res = 0
        for i in range(1, n):
            res = (res + (nums[i] - nums[i - 1]) * i * (n - i)) % mod
        return res
