from typing import Any, Optional


class Node:
    key: str
    val: Any
    pre: Optional["Node"]
    nxt: Optional["Node"]

    def __init__(self, key: str, val: Any):
        self.key, self.val = key, val
        self.pre, self.nxt = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.head, self.tail = Node("head", None), Node("tail", None)
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.length = 0

    def get(self, key: str):
        if key not in self.data:
            return -1
        node = self.data[key]
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        node.pre = self.tail.pre
        node.nxt = self.tail
        self.tail.pre.nxt = node
        self.tail.pre = node
        return node.val

    def put(self, key: str, val: Any):
        if key in self.data:
            self.get(key)
            self.data[key].val = val
            return
        if self.length == self.capacity:
            self._del(self.head.nxt.key)
        self.length += 1
        node = Node(key, val)
        self.data[key] = node
        node.pre = self.tail.pre
        node.nxt = self.tail
        self.tail.pre.nxt = node
        self.tail.pre = node

    def _del(self, key: str):
        del self.data[key]
        self.length -= 1
        node = self.head.nxt
        node.nxt.pre = self.head
        self.head.nxt = node.nxt
        del node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
