from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(people)

        def bisect_left(target: int):
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if people[mid][0] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def bisect_right(target: int):
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if people[mid][0] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        people = [(people[i], i) for i in range(n)]
        people.sort(key=lambda p: p[0])
        res = [0] * n
        
        for start, end in flowers:
            i = bisect_left(start)
            if i >= n:
                continue
            res[i] += 1
            j = bisect_right(end)
            if j + 1 < n:
                res[j + 1] -= 1
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        for i in range(n):
            idx = people[i][1]
            tmp = res[i]
            while idx != i:
                tmp, res[idx] = res[idx], tmp
                people[i], people[idx] = people[idx], people[i]
                idx = people[i][1]
            res[idx] = tmp
        return res
