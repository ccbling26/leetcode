class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        pre = ""
        res = 0
        for c in s:
            res += dic[c]
            if c == "I":
                pass
            elif c in ["V", "X"]:
                if pre == "I":
                    res -= 2 * dic["I"]
            elif c in ["L", "C"]:
                if pre == "X":
                    res -= 2 * dic["X"]
            else:
                if pre == "C":
                    res -= 2 * dic["C"]
            pre = c
        return res
