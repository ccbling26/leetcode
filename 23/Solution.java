import java.util.PriorityQueue;

class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    
    class Status implements Comparable<Status> {
        int val;
        ListNode ptr;

        Status(int val, ListNode ptr) {
            this.val = val;
            this.ptr = ptr;
        }

        @Override
        public int compareTo(Solution.Status o) {
            return this.val - o.val;
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Status> queue = new PriorityQueue<Status>();
        for (ListNode node: lists) {
            if (node != null) {
                queue.add(new Status(node.val, node));
            }
        }
        ListNode head = new ListNode(-1, null);
        ListNode cur = head;
        while (!queue.isEmpty()) {
            Status status = queue.poll();
            cur.next = status.ptr;
            cur = cur.next;
            if (status.ptr.next != null) {
                queue.add(new Status(status.ptr.next.val, status.ptr.next));
            }
        }
        return head.next;
    }
}
