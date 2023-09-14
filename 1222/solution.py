from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        tmp = [() for _ in range(9)]
        x1, y1 = king

        def check(val: int) -> int:
            if val > 0:
                return 2
            elif val < 0:
                return 0
            else:
                return 1
        for x2, y2 in queens:
            x3, y3 = x2 - x1, y2 - y1
            if x3 != 0 and y3 != 0 and abs(x3) != abs(y3):
                continue
            x, y = check(x3), check(y3)
            idx = x * 3 + y
            if not tmp[idx] or abs(x3) < abs(tmp[idx][0]) or abs(y3) < abs(tmp[idx][1]):
                tmp[idx] = (x3, y3)
        for item in tmp:
            if item:
                res.append([x1 + item[0], y1 + item[1]])
        return res
