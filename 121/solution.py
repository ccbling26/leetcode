from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = max_val = 10000
        res = 0
        for price in prices:
            if price < min_val:
                min_val = max_val = price
            elif price > max_val:
                max_val = price
                res = max(res, price - min_val)
        return res
