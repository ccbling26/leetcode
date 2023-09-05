from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        union = set(nums1) & set(nums2)
        if len(union) != 0:
            return min(union)
        x, y = min(nums1), min(nums2)
        if x > y:
            x, y = y, x
        return x * 10 + y
