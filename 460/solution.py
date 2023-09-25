class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.heap = [None] * capacity
        self.total = 0
        self.op = 0

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.op += 1
        idx, value = self.data[key]
        count, _, _ = self.heap[idx]
        self.heap[idx] = (count + 1, self.op, key)
        self._down(idx)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            idx, _ = self.data[key]
            self.data[key] = (idx, value)
            self.get(key)
            return
        self.op += 1
        if self.total == self.capacity:
            _, _, k = self.heap[0]
            del self.data[k]
            self.heap[0] = (1, self.op, key)
            self.data[key] = (0, value)
            self._down(0)
        else:
            idx = self.total
            self.total += 1
            self.heap[idx] = (1, self.op, key)
            self.data[key] = (idx, value)
            self._up(idx)

    def _up(self, idx: int):
        if idx == 0:
            return
        f = (idx - 1) // 2
        c1, o1, _ = self.heap[f]
        c2, o2, _ = self.heap[idx]
        if c1 < c2 or (c1 == c2 and o1 < o2):
            return
        else:
            self._swap(f, idx)
            self._up(f)

    def _down(self, idx: int):
        child1 = 2 * idx + 1
        child2 = child1 + 1
        if child1 >= self.total:
            return
        c1, o1, _ = self.heap[child1]
        if child2 < self.total:
            c2, o2, _ = self.heap[child2]
            if c1 > c2 or (c1 == c2 and o1 > o2):
                child1 = child2
                c1, o1 = c2, o2
        c3, o3, _ = self.heap[idx]
        if c3 > c1 or (c3 == c1 and o3 > o1):
            self._swap(idx, child1)
            self._down(child1)

    def _swap(self, idx1: int, idx2: int):
        _, _, key1 = self.heap[idx1]
        _, _, key2 = self.heap[idx2]
        _, value1 = self.data[key1]
        _, value2 = self.data[key2]
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        self.data[key1] = (idx2, value1)
        self.data[key2] = (idx1, value2)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
