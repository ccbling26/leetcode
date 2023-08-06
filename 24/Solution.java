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

    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode res = new ListNode(-1, head);
        ListNode pre = res;
        ListNode n1 = res.next, n2 = res.next.next;
        while (n1 != null && n2 != null) {
            pre.next = n2;
            n1.next = n2.next;
            n2.next = n1;
            pre = n1;
            n1 = pre.next;
            if (n1 == null) {
                break;
            }
            n2 = n1.next;
        }
        return res.next;
    }
}