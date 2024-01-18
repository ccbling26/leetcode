from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        total = sum(beans)
        res = total
        for i in range(n):
            res = min(res, total - beans[i] * (n - i))
        return res
