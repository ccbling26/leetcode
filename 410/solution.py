from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(target: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > target:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
