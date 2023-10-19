from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                counter[nums[i] * nums[j]] += 1
        res = 0
        for k, v in counter.items():
            if v >= 2:
                res += 8 * v * (v - 1) // 2
        return res
