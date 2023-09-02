from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        pre, idx = -2, -1
        res = 0
        for i in range(n):
            if forts[i] in [1, -1]:
                if pre + forts[i] == 0:
                    res = max(res, abs(i - idx) - 1)
                pre = forts[i]
                idx = i
        return res
