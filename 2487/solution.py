from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pre = None
        cur = head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            while pre.next and pre.val > pre.next.val:
                pre.next = pre.next.next
        cur = pre
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
