from bisect import bisect
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        counter1 = [0] * n
        counter2 = defaultdict(int)
        for x, y in edges:
            x -= 1
            y -= 1
            if x > y:
                x, y = y, x
            counter1[x] += 1
            counter1[y] += 1
            counter2[x * n + y] += 1
        arr = sorted(counter1)
        res = []
        for item in queries:
            total = 0
            for i in range(n):
                j = bisect(arr, item - arr[i]) - 1
                total += n - 1 - max(i, j)
            for k, v in counter2.items():
                x, y = k // n, k % n
                if counter1[x] + counter1[y] > item and counter1[x] + counter1[y] - v <= item:
                    total -= 1
            res.append(total)
        return res
