
class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int added = 0;
        ListNode head = new ListNode(-1, null);
        ListNode tmp = head;
        while (l1 != null || l2 != null) {
            int val = added;
            if (l1 != null) {
                val += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                val += l2.val;
                l2 = l2.next;
            }
            tmp.next = new ListNode(val % 10, null);
            tmp = tmp.next;
            added = val / 10;
        }
        if (added != 0) {
            tmp.next = new ListNode(added, null);
        }
        return head.next;
    }
}