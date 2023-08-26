from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        if n == 0:
            return res
        tmp = [str(nums[0]), ""]
        for i in range(1, n):
            if nums[i] - 1 != nums[i - 1]:
                if tmp[1] == "":
                    res.append(tmp[0])
                else:
                    res.append(tmp[0] + "->" + tmp[1])
                tmp = [str(nums[i]), ""]
            else:
                tmp[1] = str(nums[i])
        if tmp[1] == "":
            res.append(tmp[0])
        else:
            res.append(tmp[0] + "->" + tmp[1])
        return res
