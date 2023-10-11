from collections import defaultdict
from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        scores = defaultdict(int)
        for item in positive_feedback:
            scores[item] = 3
        for item in negative_feedback:
            scores[item] = -1
        n = len(report)
        h = []
        for i in range(n):
            tmp = 0
            for w in report[i].split(" "):
                tmp += scores[w]
            h.append((tmp, student_id[i]))
        h.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i in range(k):
            res.append(h[i][1])
        return res
