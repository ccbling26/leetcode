from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        i = 0
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp == target:
                return [i + 1, j + 1]
            elif tmp > target:
                j -= 1
            else:
                i += 1
        return []
