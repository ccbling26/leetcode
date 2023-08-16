from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        step = k
        flag = [False] * n
        idx = 0
        flag[idx] = True
        while True:
            idx = (idx + step) % n
            if flag[idx]:
                break
            flag[idx] = True
            step += k
        res = []
        for i in range(n):
            if not flag[i]:
                res.append(i + 1)
        return res
