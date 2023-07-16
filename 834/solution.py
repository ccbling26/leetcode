from collections import defaultdict, deque
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_dict = defaultdict(list)
        for x, y in edges:
            edge_dict[x].append(y)
            edge_dict[y].append(x)

        dp = [0] * n
        sz = [0] * n
        
        def dfs_1(child: int, father: int):
            sz[child] = 1
            for item in edge_dict[child]:
                if item == father:
                    continue
                dfs_1(item, child)
                dp[child] += dp[item] + sz[item]
                sz[child] += sz[item]
        
        dfs_1(0, -1)

        res = [0] * n
        def dfs_2(child: int, father: int):
            res[child] = dp[child]
            for item in edge_dict[child]:
                if item == father:
                    continue
                pu, pv = dp[child], dp[item]
                su, sv = sz[child], sz[item]
                dp[child] -= dp[item] + sz[item]
                sz[child] -= sz[item]
                dp[item] += dp[child] + sz[child]
                sz[item] += sz[child]

                dfs_2(item, child)

                dp[child], dp[item] = pu, pv
                sz[child], sz[item] = su, sv
        
        dfs_2(0, -1)
        
        return res
