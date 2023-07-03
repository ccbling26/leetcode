from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q1, q2 = [], []
        head = ListNode(-1)
        while l1:
            q1.append(l1)
            l1 = l1.next
        while l2:
            q2.append(l2)
            l2 = l2.next
        added = 0
        while q1 or q2:
            val = added
            if q1:
                val += q1.pop().val
            if q2:
                val += q2.pop().val
            tmp = ListNode(val % 10, head.next)
            head.next = tmp
            added = val // 10
        if added:
            return ListNode(added, head.next)
        return head.next