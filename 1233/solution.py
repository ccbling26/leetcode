from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        n = len(folder)
        for i in range(1, n):
            l = len(ans[-1])
            if not (l < len(folder[i]) and ans[-1] == folder[i][:l] and folder[i][l] == "/"):
                ans.append(folder[i])
        return ans
