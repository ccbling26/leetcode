from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def find(l: int, r: int) -> int:
            if l > r:
                return l
            nonlocal nums
            nonlocal target
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return find(l, mid - 1)
            else:
                return find(mid + 1, r)
        return find(0, len(nums) - 1)
