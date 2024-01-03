
class Solution {
    public ListNode removeNodes(ListNode head) {
        ListNode pre = null, nxt = null;
        ListNode cur = head;
        while (cur != null) {
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
            while (pre.next != null && pre.val > pre.next.val) {
                pre.next = pre.next.next;
            }
        }
        cur = pre;
        pre = null;
        while (cur != null) {
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
}

class ListNode {
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