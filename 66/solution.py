from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        added = 1
        idx = len(digits) - 1
        while idx >= 0 and added != 0:
            digits[idx] += added
            added = digits[idx] // 10
            digits[idx] %= 10
            idx -= 1
        if added != 0:
            digits = [added, *digits]
        return digits
