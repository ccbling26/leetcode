class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        relations1 = {}
        relations2 = {}
        n = len(s)
        for i in range(n):
            x = s[i]
            y = t[i]
            if x in relations1:
                if relations1[x] != y:
                    return False
            elif y in relations2:
                if relations2[y] != x:
                    return False
            else:
                relations1[x] = y
                relations2[y] = x
        return True
