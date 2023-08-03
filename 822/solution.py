from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        keys = set()
        not_allow = set()
        for i in range(n):
            keys.add(fronts[i])
            keys.add(backs[i])
            if fronts[i] == backs[i]:
                not_allow.add(fronts[i])
        res = 2001
        for k in keys:
            if k not in not_allow:
                res = min(res, k)
        return 0 if res == 2001 else res
