class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode tmp1 = new ListNode(0, head);
        ListNode tmp2 = tmp1;
        for (int i = 1; i < left; i++) {
            tmp2 = tmp2.next;
        }
        ListNode cur = tmp2.next;
        ListNode pre = null, nxt = null;
        for (int i = 0; i <= right - left; i++) {
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        tmp2.next = pre;
        while (tmp2.next != null) {
            tmp2 = tmp2.next;
        }
        tmp2.next = nxt;
        return tmp1.next;
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