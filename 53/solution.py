from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = res = nums[0]

        for num in nums[1:]:
            cur = max(num, cur + num)
            res = max(cur, res)

        return res