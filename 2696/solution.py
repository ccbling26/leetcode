class Solution:
    def minLength(self, s: str) -> int:
        arr = []
        for item in s:
            if item == 'B' and arr and arr[-1] == "A":
                arr.pop()
            elif item == "D" and arr and arr[-1] == "C":
                arr.pop()
            else:
                arr.append(item)
        return len(arr)
