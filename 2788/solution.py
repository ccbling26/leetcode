from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        m = len(separator)
        for word in words:
            i = j = 0
            n = len(word)
            while j < n:
                if word[j] == separator[0]:
                    if word[j:j + m] == separator:
                        if i != j:
                            res.append(word[i:j])
                        i = j + m
                        j = j + m
                else:
                    j += 1
            if i != j:
                res.append(word[i:j])
        return res
