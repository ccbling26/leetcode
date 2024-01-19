from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        dp = [0] * (n + 1)
        for j, (b, a) in enumerate(sorted(zip(nums2, nums1)), 1):
            for i in range(j, 0, -1):
                dp[i] = max(dp[i], dp[i - 1] + i * b + a)
        sa, sb = sum(nums1), sum(nums2)
        for i in range(n + 1):
            if sb * i + sa - dp[i] <= x:
                return i
        return -1
