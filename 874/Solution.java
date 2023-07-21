import java.util.HashSet;

class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0, y = 0, d = 0, res = 0;
        HashSet<String> hashSet = new HashSet<>();
        for (int[] obstacle: obstacles) {
            hashSet.add(String.format("%d_%d", obstacle[0], obstacle[1]));
        }
        for (int command: commands) {
            if (command < 0) {
                d += command == -1 ? 1: 3;
                d %= 4;
            } else {
                for (int i = 0; i < command; i++) {
                    int tx = x + dirs[d][0];
                    int ty = y + dirs[d][1];
                    if (hashSet.contains(String.format("%d_%d", tx, ty))) {
                        break;
                    }
                    x = tx;
                    y = ty;
                    res = Math.max(res, x * x + y * y);
                }
            }
        }
        return res;
    }
}