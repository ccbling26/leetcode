class Solution:
    def splitNum(self, num: int) -> int:
        stnum = sorted(str(num))
        num1, num2 = int("".join(stnum[::2])), int("".join(stnum[1::2]))
        return num1 + num2
