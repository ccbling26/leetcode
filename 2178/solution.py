from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        i = 2
        res = []
        while i <= finalSum:
            res.append(i)
            finalSum -= i
            i += 2
        res[-1] += finalSum
        return res
