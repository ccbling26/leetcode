from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        res = 0
        for k, v in counter1.items():
            if v == 1 and counter2[k] == 1:
                res += 1
        return res
