from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        tmp = set()
        for item in words:
            if item in tmp:
                res += 1
            else:
                item = item[::-1]
                tmp.add(item)
        return res
