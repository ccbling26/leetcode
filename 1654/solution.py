from collections import deque
import sys
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        n = 1 + max(max(forbidden) + a, x) + b
        visited = set([0])
        dp = [sys.maxsize] * n
        dp[0] = 0
        for item in forbidden:
            if item < n:
                dp[item] = -1
        q = deque([(0, 1)])
        while q:
            pos, d = q.popleft()
            if pos == x:
                return dp[pos]
            pos1 = pos + a
            pos2 = pos - b
            if pos1 < n and dp[pos1] != -1 and pos1 not in visited:
                visited.add(pos1)
                dp[pos1] = 1 + dp[pos]
                q.append((pos1, 1))
            if d == 1:
                if pos2 >= 0 and dp[pos2] != -1 and pos2 * (-1) not in visited:
                    visited.add(pos2 * -1)
                    dp[pos2] = 1 + dp[pos]
                    q.append((pos2, -1))
        return -1
