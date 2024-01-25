from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        res = 0
        prefix, suffix = [0] * n, [0] * n
        stack1, stack2 = [], []

        for i in range(n):
            while stack1 and maxHeights[i] < maxHeights[stack1[-1]]:
                stack1.pop()
            if stack1:
                prefix[i] = prefix[stack1[-1]] + (i - stack1[-1]) * maxHeights[i]
            else:
                prefix[i] = (i + 1) * maxHeights[i]
            stack1.append(i)

        for i in range(n - 1, -1, -1):
            while stack2 and maxHeights[i] < maxHeights[stack2[-1]]:
                stack2.pop()
            if stack2:
                suffix[i] = suffix[stack2[-1]] + (stack2[-1] - i) * maxHeights[i]
            else:
                suffix[i] = (n - i) * maxHeights[i]
            stack2.append(i)
            res = max(res, prefix[i] + suffix[i] - maxHeights[i])

        return res
