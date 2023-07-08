import heapq
import sys

from typing import List


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        wait_left = []
        wait_right = []
        work_left = []
        work_right = []

        for i, item in enumerate(time):
            # time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi]
            heapq.heappush(wait_left, (-(item[0] + item[2]), -i))
        
        remain = n
        cur_time = 0
        
        while remain > 0 or len(work_right) or len(wait_right):
            while len(work_left) and work_left[0][0] <= cur_time:
                item = heapq.heappop(work_left)
                idx = item[1]
                heapq.heappush(wait_left, (-(time[idx][0] + time[idx][2]), -idx))
            while len(work_right) and work_right[0][0] <= cur_time:
                item = heapq.heappop(work_right)
                idx = item[1]
                heapq.heappush(wait_right, (-(time[idx][0] + time[idx][2]), -idx))
            if len(wait_right):
                item = heapq.heappop(wait_right)
                idx = -item[1]
                cur_time += time[idx][2]
                heapq.heappush(work_left, (cur_time + time[idx][3], idx))
            elif remain > 0 and len(wait_left):
                item = heapq.heappop(wait_left)
                idx = -item[1]
                cur_time += time[idx][0]
                heapq.heappush(work_right, (cur_time + time[idx][1], idx))
                remain -= 1
            else:
                tmp = sys.maxsize
                if len(work_left):
                    tmp = min(tmp, work_left[0][0])
                if len(work_right):
                    tmp = min(tmp, work_right[0][0])
                if tmp != sys.maxsize:
                    cur_time = max(cur_time, tmp)
        return cur_time
