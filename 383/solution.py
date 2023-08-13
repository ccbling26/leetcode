from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for c in ransomNote:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1
        return True
