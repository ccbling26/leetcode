class Solution:
    def alternateDigitSum(self, n: int) -> int:
        prefix = 1
        res = 0
        while n:
            res += prefix * (n % 10)
            prefix *= -1
            n //= 10
        return -1 * prefix * res
