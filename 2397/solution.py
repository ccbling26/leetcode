from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        new_matrix = []
        for arr in matrix:
            num = 0
            for item in arr:
                num <<= 1
                if item:
                    num |= 1
            new_matrix.append(num)
        res = 0

        def find(num):
            nonlocal res
            nonlocal new_matrix

            tmp = 0
            for item in new_matrix:
                if num | item == num:
                    tmp += 1
            res = max(res, tmp)

        n = len(matrix[0])

        def get_num(i, s, num):
            nonlocal n
            if i == n and s != 0:
                return
            elif i == n and s == 0:
                find(num)
                return
            get_num(i + 1, s, num << 1)
            get_num(i + 1, s - 1, num << 1 | 1)

        get_num(0, numSelect, 0)

        return res
