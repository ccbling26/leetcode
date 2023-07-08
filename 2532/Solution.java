import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    private static int[][] time;

    static Comparator<Integer> waitPriority = (x, y) -> {
        int timeX = time[x][0] + time[x][2];
        int timeY = time[y][0] + time[y][2];
        return timeX == timeY ? y - x : timeY - timeX;
    };

    static Comparator<int[]> workPriority = (x, y) -> x[0] == y[0] ? x[1] - y[1] : x[0] - y[0];

    public int findCrossingTime(int n, int k, int[][] time) {
        Solution.time = time;
        PriorityQueue<Integer> waitLeft = new PriorityQueue<>(waitPriority);
        PriorityQueue<Integer> waitRight = new PriorityQueue<>(waitPriority);
        PriorityQueue<int[]> workLeft = new PriorityQueue<>(workPriority);
        PriorityQueue<int[]> workRight = new PriorityQueue<>(workPriority);

        for (int i = 0; i < k; i++) {
            waitLeft.offer(i);
        }

        int remain = n;
        int curTime = 0;

        while (remain > 0 || !workRight.isEmpty() || !waitRight.isEmpty()) {
            while (!workLeft.isEmpty() && workLeft.peek()[0] <= curTime) {
                waitLeft.offer(workLeft.poll()[1]);
            }
            while (!workRight.isEmpty() && workRight.peek()[0] <= curTime) {
                waitRight.offer(workRight.poll()[1]);
            }
            if (!waitRight.isEmpty()) {
                int idx = waitRight.poll();
                curTime += time[idx][2];
                workLeft.offer(new int[]{curTime + time[idx][3], idx});
            } else if (remain > 0 && !waitLeft.isEmpty()) {
                remain--;
                int idx = waitLeft.poll();
                curTime += time[idx][0];
                workRight.offer(new int[]{curTime + time[idx][1], idx});
            } else {
                int nextTime = Integer.MAX_VALUE;
                if (!workLeft.isEmpty()) {
                    nextTime = Math.min(nextTime, workLeft.peek()[0]);
                }
                if (!workRight.isEmpty()) {
                    nextTime = Math.min(nextTime, workRight.peek()[0]);
                }
                if (nextTime != Integer.MAX_VALUE) {
                    curTime = Math.max(nextTime, curTime);
                }
            }
        }
        return curTime;
    }
}
