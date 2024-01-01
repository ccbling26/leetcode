from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        min_round, cur_round, max_profits, cur_profits, rest_num = 0, 0, 0, 0, 0
        i, n = 0, len(customers)
        while i < n or rest_num:
            if i < n:
                rest_num += customers[i]
                i += 1
            cur_profits += min(4, rest_num) * boardingCost - runningCost
            cur_round += 1
            if cur_profits > max_profits:
                max_profits = cur_profits
                min_round = cur_round
            rest_num -= min(rest_num, 4)
        return min_round if min_round else -1
