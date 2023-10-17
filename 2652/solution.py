class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def f(m: int) -> int:
            count = n // m
            return (m + m * count) * count // 2
        return f(3) + f(5) + f(7) - f(15) - f(21) - f(35) + f(105)
