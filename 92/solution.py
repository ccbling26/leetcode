from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmp1 = ListNode(0, head)
        tmp2 = tmp1
        for i in range(left - 1):
            tmp2 = tmp2.next
        cur = tmp2.next
        pre = nxt = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        tmp2.next = pre
        while tmp2.next:
            tmp2 = tmp2.next
        tmp2.next = nxt
        return tmp1.next
