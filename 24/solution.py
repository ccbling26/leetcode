from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = ListNode(-1, head)
        pre = res
        n1 = pre.next
        n2 = n1.next
        while n1 and n2:
            pre.next = n2
            n1.next = n2.next
            n2.next = n1
            pre = n1
            n1 = pre.next
            if not n1:
                break
            n2 = n1.next
        return res.next
