from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n, m = len(s), len(wordDict)
        dp = [[] for _ in range(n + 1)]
        dp[0] = True
        words = {wordDict[i]: i for i in range(m)}
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j]:
                    val = s[j:i]
                    if val in words:
                        dp[i].append(words[val])

        def find(idx: int):
            if idx == 0:
                return [""]
            res = []
            for item in dp[idx]:
                pre = find(idx - len(wordDict[item]))
                for p in pre:
                    if p:
                        res.append(p + " " + wordDict[item])
                    else:
                        res.append(wordDict[item])
            return res
        return find(n)
