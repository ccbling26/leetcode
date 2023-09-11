import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda p: p[1])
        q = list()
        total = 0
        for d, l in courses:
            if total + d <= l:
                total += d
                heapq.heappush(q, -d)
            elif q and -q[0] > d:
                total -= -q[0] - d
                heapq.heappop(q)
                heapq.heappush(q, -d)
        return len(q)
