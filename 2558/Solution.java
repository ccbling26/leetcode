import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2.compareTo(o1);
            }
        });
        for (int gift : gifts) {
            queue.offer(gift);
        }
        for (int i = 0; i < k; i++) {
            queue.offer((int) Math.sqrt(queue.poll()));
        }
        long res = 0;
        while (!queue.isEmpty()) {
            res += queue.poll();
        }
        return res;
    }
}