class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        res = 0
        i = j = 0
        n = len(s)
        while j < n:
            c = s[j]
            while i < j and c in hash_set:
                hash_set.discard(s[i])
                i += 1
            hash_set.add(c)
            j += 1
            res = max(res, j - i)
        return res
