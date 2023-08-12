class Solution:
    def isValid(self, s: str) -> bool:
        relations = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        tmp = []
        for c in s:
            if c in ['(', '[', '{']:
                tmp.append(c)
            elif len(tmp) == 0:
                return False
            elif tmp[-1] != relations[c]:
                return False
            else:
                tmp.pop()
        return len(tmp) == 0
