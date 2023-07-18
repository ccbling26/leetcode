import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        Integer[] qindex = new Integer[queries.length];
        for (int i = 0; i < queries.length; i++) {
            qindex[i] = i;
        }
        Arrays.sort(qindex, (x, y) -> queries[x] - queries[y]);
        Arrays.sort(intervals, (x, y) -> x[0] - y[0]);
        PriorityQueue<int[]> queue = new PriorityQueue<>((x, y) -> {
            return x[0] - y[0];
        });
        int[] res = new int[queries.length];
        Arrays.fill(res, -1);
        int idx = 0;
        for (int q: qindex) {
            while (idx < intervals.length && intervals[idx][0] <= queries[q]) {
                int begin = intervals[idx][0], end = intervals[idx][1];
                int length = end - begin + 1;
                queue.offer(new int[]{length, end});
                idx++;
            }
            while (!queue.isEmpty() && queue.peek()[1] < queries[q]) {
                queue.poll();
            }
            if (!queue.isEmpty()) {
                res[q] = queue.peek()[0];
            }
        }
        return res;
    }
}
