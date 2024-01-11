class Solution:
    def addMinimum(self, word: str) -> int:
        item = ["a", "b", "c"]
        cnt = 0
        i = 0
        for c in word:
            while c != item[i]:
                cnt += 1
                i = (i + 1) % 3
            i = (i + 1) % 3
        return cnt if i == 0 else cnt + 3 - i
