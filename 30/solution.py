from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n, l, res = len(s), len(words), len(words[0]), []
        if n * l > m:
            return res
        for i in range(l):
            j, k = i, i
            count = 0
            counter = Counter(words)
            while k + l <= m:
                word = s[k:k+l]
                if word not in words:
                    j, k = k + l, k + l
                    counter = Counter(words)
                    count = 0
                    continue
                while counter[word] == 0:
                    counter[s[j:j+l]] += 1
                    j += l
                    count -= 1
                counter[word] -= 1
                count += 1
                k += l
                if count == n:
                    res.append(j)
                    counter[s[j:j+l]] += 1
                    j += l
                    count -= 1
        return res
