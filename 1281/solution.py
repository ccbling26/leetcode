class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = 1
        b = 0
        while n != 0:
            c = n % 10
            n //= 10
            a *= c
            b += c
        return a - b
