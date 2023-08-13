class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            val = mid ** 2
            if val == x:
                return mid
            elif val < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
