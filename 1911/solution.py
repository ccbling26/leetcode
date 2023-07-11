from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        for num in nums:
            even, odd = max(even, odd + num), max(odd, even - num)
        return even
