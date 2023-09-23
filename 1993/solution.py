from collections import defaultdict, deque
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.n = len(parent)
        self.parent = parent
        self.children = defaultdict(list)
        for i in range(self.n):
            self.children[self.parent[i]].append(i)
        self.locks = [0] * self.n

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] != 0:
            return False
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == 0 or self.locks[num] != user:
            return False
        self.locks[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locks[num] != 0:
            return False
        flag = False
        q = deque([*self.children[num]])
        tmp = []
        while q:
            idx = q.popleft()
            if idx >= self.n:
                continue
            if self.locks[idx] != 0:
                flag = True
                tmp.append(idx)
            q.extend(self.children[idx])
        if not flag:
            return False
        idx = self.parent[num]
        while idx >= 0:
            if self.locks[idx] != 0:
                return False
            idx = self.parent[idx]
        self.locks[num] = user
        for item in tmp:
            self.locks[item] = 0
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
