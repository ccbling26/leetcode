from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = 1
        inc, dec, pre = 1, 0, 1
        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                inc = pre
                res += inc
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                res += dec
                pre = 1
        return res
