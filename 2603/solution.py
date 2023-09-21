from collections import defaultdict, deque
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        edge_dict = defaultdict(list)
        degree = [0] * n
        for p, q in edges:
            edge_dict[p].append(q)
            edge_dict[q].append(p)
            degree[p] += 1
            degree[q] += 1

        rest = n
        q = deque([i for i in range(n) if degree[i] == 1 and coins[i] == 0])
        while q:
            i = q.popleft()
            degree[i] -= 1
            rest -= 1
            for j in edge_dict[i]:
                degree[j] -= 1
                if degree[j] == 1 and coins[j] == 0:
                    q.append(j)

        for _ in range(2):
            q = deque([i for i in range(n) if degree[i] == 1])
            while q:
                i = q.popleft()
                degree[i] -= 1
                rest -= 1
                for j in edge_dict[i]:
                    degree[j] -= 1

        return 0 if rest == 0 else (rest - 1) * 2
