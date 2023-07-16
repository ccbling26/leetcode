from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        for _ in range(n):
            p1 = p1.next
        if not p1:
            return head.next
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        del_node = p2.next
        p2.next = del_node.next
        return head
