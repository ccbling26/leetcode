from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        for l, r, c in bookings:
            res[l - 1] += c
            res[r] -= c
        for i in range(1, n + 1):
            res[i] += res[i - 1]
        return res[:n]
