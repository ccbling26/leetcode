from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        check = [False] * numCourses
        pre = defaultdict(list)
        for p, q in prerequisites:
            pre[q].append(p)
        pre_sum = defaultdict(set)

        def find(idx: int):
            if check[idx]:
                return pre_sum[idx]
            tmp = set()
            for i in pre[idx]:
                tmp.add(i)
                for item in find(i):
                    tmp.add(item)
            pre_sum[idx] = tmp
            check[idx] = True
            return tmp

        for i in range(numCourses):
            find(i)

        res = []
        for p, q in queries:
            res.append(p in pre_sum[q])
        return res
