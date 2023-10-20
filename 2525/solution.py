class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        base1 = 10 ** 4
        base2 = 10 ** 9
        bulky = length >= base1 or width >= base1 or height >= base1 or width * height * length >= base2
        heavy = mass >= 100
        if bulky:
            return "Bulky" if not heavy else "Both"
        else:
            return "Heavy" if heavy else "Neither"
