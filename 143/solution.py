from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid = self.findMiddle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        self.merge(l1, l2)

    def findMiddle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def merge(self, l1: ListNode, l2: ListNode):
        cur = l1
        while l2:
            tmp = l2
            l2 = l2.next
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next.next
