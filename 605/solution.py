from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, j = -2, 0
        m = len(flowerbed)
        res = 0
        while j < m:
            if flowerbed[j] == 1:
                res += (max(j - i - 2, 0)) // 2
                i = j
            j += 1
        res += (max(m - i - 1, 0) // 2)
        return res >= n
