import java.util.Stack;

class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        int added = 0;
        ListNode head = new ListNode(-1, null);
        
        while (!s1.empty() || !s2.empty()) {
            int val = added;
            if (!s1.empty()) {
                val += s1.pop();
            }
            if (!s2.empty()) {
                val += s2.pop();
            }
            head.next = new ListNode(val % 10, head.next);
            added = val / 10;
        }
        if (added != 0) {
            return new ListNode(added, head.next);
        }
        return head.next;
    }
}