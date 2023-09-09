from collections import defaultdict
from typing import List


class Solution:
    def check(self, i: int):
        if self.tmp[i]:
            return True
        if self.flags[i]:
            return False
        self.flags[i] = True
        for item in self.needs[i]:
            if not self.check(item):
                return False
        self.flags[i] = False
        self.tmp[i] = True
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.needs = defaultdict(list)
        for x, y in prerequisites:
            self.needs[x].append(y)
        self.flags = [False] * numCourses
        self.tmp = [False] * numCourses
        for i in range(numCourses):
            if not self.check(i):
                return False
        return True
