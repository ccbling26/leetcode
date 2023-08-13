class Solution {
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode cur = head;
        ListNode nxt = head.next;
        while (nxt != null) {
            while (nxt != null && cur.val == nxt.val) {
                nxt = nxt.next;
                cur.next = nxt;
            }
            if (nxt != null) {
                cur = nxt;
                nxt = nxt.next;
            }
        }
        return head;
    }
}