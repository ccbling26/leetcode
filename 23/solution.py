from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Heapq:
    def __init__(self, n: int):
        self.arr = [None] * (n + 1)
        self.length = 0

    def push(self, obj: ListNode):
        self.length += 1
        self.arr[self.length] = obj
        self.up(self.length)
    
    def pop(self):
        self.arr[1], self.arr[self.length] = self.arr[self.length], self.arr[1]
        res = self.arr[self.length]
        self.length -= 1
        self.down(1)
        return res
    
    def up(self, idx: int):
        if idx == 1:
            return
        father_idx = idx // 2
        if self.arr[idx].val < self.arr[father_idx].val:
            self.arr[idx], self.arr[father_idx] = self.arr[father_idx], self.arr[idx]
            self.up(father_idx)

    def down(self, idx: int):
        left_idx = idx * 2
        if left_idx <= self.length and self.arr[left_idx].val < self.arr[idx].val:
            self.arr[idx], self.arr[left_idx] = self.arr[left_idx], self.arr[idx]
            self.down(left_idx)
        right_idx = idx * 2 + 1
        if right_idx <= self.length and self.arr[right_idx].val < self.arr[idx].val:
            self.arr[idx], self.arr[right_idx] = self.arr[right_idx], self.arr[idx]
            self.down(right_idx)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = Heapq(len(lists))
        for item in lists:
            if item:
                heap.push(item)
        head = cur = ListNode()
        while heap.length != 0:
            tmp = heap.pop()
            cur.next = tmp
            cur = cur.next
            if tmp.next:
                heap.push(tmp.next)
        return head.next
