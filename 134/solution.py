from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, res, total, idx = len(gas), 0, 0, 0
        for i in range(n):
            val = gas[i] - cost[i]
            total += val
            res += val
            if res < 0:
                res = 0
                idx = i + 1
        if total < 0:
            return -1
        return idx
