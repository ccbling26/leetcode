import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        int res = Integer.MIN_VALUE;
        Deque<int[]> queue = new LinkedList<>();
        for (int[] point: points) {
            int x = point[0], y = point[1];
            while (queue.size() > 0 && x - queue.getFirst()[1] > k) {
                queue.removeFirst();
            }
            if (queue.size() > 0) {
                res = Math.max(res, x + y + queue.getFirst()[0]);
            }
            while (queue.size() > 0 && y - x >= queue.getLast()[0]) {
                queue.removeLast();
            }
            queue.add(new int[]{y - x, x});
        }
        return res;
    }
}