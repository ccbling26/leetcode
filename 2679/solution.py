class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            nums[i].sort()
        res = 0
        for i in range(len(nums[0])):
            tmp = 0
            for j in range(len(nums)):
                tmp = max(tmp, nums[j][i])
            res += tmp
        return res
