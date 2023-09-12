from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1002
        m = 0
        for n, f, t in trips:
            arr[f + 1] += n
            arr[t + 1] -= n
            m = max(m, t + 1)
        for i in range(1, m + 1):
            arr[i] += arr[i - 1]
            if arr[i] > capacity:
                return False
        return True
