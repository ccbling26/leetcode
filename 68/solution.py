from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)
        while i < n:
            left = i
            l = 0
            while i < n and l + len(words[i]) + i - left <= maxWidth:
                l += len(words[i])
                i += 1
            black_count = maxWidth - l
            if i == n:
                res.append(" ".join(words[left:]) + " "*(black_count - i + left + 1))
                break
            count = i - left
            if count == 1:
                res.append(words[left] + " "*black_count)
            else:
                item = ""
                avg = black_count // (count - 1)
                more = black_count % (count - 1)
                for j in range(more):
                    item += words[left + j] + " " * (avg + 1)
                res.append(item + (" "*avg).join(words[left + more:i]))
        return res