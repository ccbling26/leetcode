from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        a, b = newInterval[0], newInterval[1]
        while i < n:
            item = intervals[i]
            if item[1] < a:
                res.append(item)
            elif item[0] > b:
                res.append([a, b])
                res.extend(intervals[i:])
                return res
            elif item[0] == b:
                res.append([a, item[1]])
                res.extend(intervals[i + 1:])
                return res
            else:
                a = min(item[0], a)
                b = max(item[1], b)
            i += 1
        res.append([a, b])
        return res
