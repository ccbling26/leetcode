from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res:
                res.append(num)
            flag = False
            for i in range(len(res)):
                if num <= res[i]:
                    res[i] = num
                    flag = True
                    break
            if not flag:
                res.append(num)
        return len(res)
