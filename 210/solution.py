from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        need = defaultdict(list)
        for x, y in prerequisites:
            need[x].append(y)

        res = []
        flags = [0] * numCourses
        invalid = False

        def find(idx: int):
            nonlocal invalid
            if invalid:
                return False
            if flags[idx] == 1:
                invalid = True
                return False
            elif flags[idx] == 2:
                return True
            flags[idx] = 1
            for item in need[idx]:
                if not find(item):
                    return False
            res.append(idx)
            flags[idx] = 2
            return True

        for i in range(numCourses):
            if not find(i):
                break
        return res if not invalid else []
