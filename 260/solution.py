from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp = 0
        for num in nums:
            tmp ^= num
        i = 1
        while i & tmp == 0:
            i <<= 1
        a, b = 0, 0
        for num in nums:
            if num & i:
                a ^= num
            else:
                b ^= num
        return [a, b]
