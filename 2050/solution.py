from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prev = [[] for _ in range(n)]
        for x, y in relations:
            prev[y - 1].append(x - 1)
        dp_dict = {}

        def dp(idx: int) -> int:
            if idx in dp_dict:
                return dp_dict[idx]
            cur = 0
            for i in prev[idx]:
                cur = max(cur, dp(i))
            cur += time[idx]
            dp_dict[idx] = cur
            return cur

        res = 0
        for i in range(n):
            res = max(res, dp(i))
        return res
