from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n + 1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        res = 0
        for i in range(n, -1, -1):
            res += counter[i]
            if res >= i:
                return i
        return 0
