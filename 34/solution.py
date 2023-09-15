from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def search(left: int, right: int, is_left: bool):
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    if is_left:
                        if mid == 0 or nums[mid-1] < target:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        if mid == n-1 or nums[mid+1] > target:
                            return mid
                        else:
                            left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        l = search(0, n - 1, True)
        if l == -1:
            return [-1, -1]
        else:
            return [l, search(l, n - 1, False)]
