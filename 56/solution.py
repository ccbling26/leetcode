from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        tmp = intervals[0]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] > tmp[1]:
                res.append(tmp)
                tmp = intervals[i]
            else:
                tmp[1] = max(tmp[1], intervals[i][1])
        res.append(tmp)
        return res
