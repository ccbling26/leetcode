from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        l = head
        r = head.next
        while r:
            while r and l.val == r.val:
                r = r.next
                l.next = r
            if r:
                l = r
                r = r.next
        return head
