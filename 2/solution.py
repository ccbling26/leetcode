from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added = 0
        head = tmp = ListNode(-1)
        while l1 or l2:
            val = added
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            tmp.next = ListNode(val % 10)
            tmp = tmp.next
            added = val // 10
        if added:
            tmp.next = ListNode(added)
        return head.next
