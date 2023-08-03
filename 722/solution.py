from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        is_block = False
        new_line = []
        for item in source:
            i = 0
            n = len(item)
            while i < n:
                if is_block:
                    if i + 1 < n and item[i] == "*" and item[i + 1] == "/":
                        is_block = False
                        i += 1
                else:
                    if i + 1 < n and item[i] == "/" and item[i + 1] == "*":
                        is_block = True
                        i += 1
                    elif i + 1 < n and item[i] == "/" and item[i + 1] == "/":
                        break
                    else:
                        new_line.append(item[i])
                i += 1
            if not is_block and len(new_line):
                res.append("".join(new_line))
                new_line = []
        return res
