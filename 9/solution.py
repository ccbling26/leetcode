class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        while y < x:
            y *= 10
            y += x % 10
            x //= 10
        return x == y or x == y//10
