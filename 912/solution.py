from typing import List


class Solution:
    def sort(self, i: int, j: int):
        if i >= j:
            return
        elif i + 1 == j:
            if self.nums[i] > self.nums[j]:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        else:
            mid = (i + j) // 2
            self.sort(i, mid)
            self.sort(mid + 1, j)
            self.merge(i, mid + 1, j)

    def merge(self, i: int, j: int, k: int):
        tmp = []
        a = i
        b = j
        while a < j and b <= k:
            if self.nums[a] <= self.nums[b]:
                tmp.append(self.nums[a])
                a += 1
            else:
                tmp.append(self.nums[b])
                b += 1
        while a < j:
            tmp.append(self.nums[a])
            a += 1
        while b <= k:
            tmp.append(self.nums[b])
            b += 1
        for j in range(len(tmp)):
            self.nums[i + j] = tmp[j]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.sort(0, len(nums) - 1)
        return self.nums
