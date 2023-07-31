class Solution {
    public void reorderList(ListNode head) {
        if (head == null) {
            return;
        }

        ListNode mid = findMiddle(head);
        ListNode l1 = head;
        ListNode l2 = mid.next;
        mid.next = null;

        l2 = reverse(l2);
        merge(l1, l2);
    }

    public ListNode findMiddle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode nxt = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nxt;
        }
        return prev;
    }

    public void merge(ListNode l1, ListNode l2) {
        ListNode cur = l1;
        while (l2 != null) {
            ListNode tmp = l2;
            l2 = l2.next;
            tmp.next = cur.next;
            cur.next = tmp;
            cur = cur.next.next;
        }
    }

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
}