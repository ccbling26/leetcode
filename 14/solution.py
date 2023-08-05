from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        lengths = []
        for i in range(n):
            lengths.append(len(strs[i]))
        res = ""
        i = 0
        l = 1
        cur = ' '
        while True:
            if l > lengths[i]:
                break
            if cur == ' ':
                cur = strs[i][l - 1]
            elif strs[i][l - 1] != cur:
                break
            i += 1
            if i == n:
                i = 0
                res += cur
                cur = ' '
                l += 1
        return res
