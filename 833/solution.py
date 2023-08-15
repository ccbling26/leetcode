from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replace = [(c, 1) for c in s]
        for indice, source, target in zip(indices, sources, targets):
            if s.startswith(source, indice):
                replace[indice] = (target, len(source))
        ans = []
        i = 0
        while i < len(s):
            ans.append(replace[i][0])
            i += replace[i][1]
        return "".join(ans)
