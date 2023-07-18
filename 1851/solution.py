import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        intervals_heap = []
        res = [-1] * len(queries)

        i = 0
        for query_idx, query_val in sorted_queries:
            while i < len(sorted_intervals) and sorted_intervals[i][0] <= query_val:
                begin, end = sorted_intervals[i]
                length = end - begin + 1
                heapq.heappush(intervals_heap, (length, end))
                i += 1
            while intervals_heap and intervals_heap[0][1] < query_val:
                heapq.heappop(intervals_heap)
            if intervals_heap:
                res[query_idx] = intervals_heap[0][0]
        return res
