class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] path = new int[1001];
        for (int[] trip: trips) {
            int num = trip[0], from = trip[1], to = trip[2];
            path[from] += num;
            path[to] -= num;
        }
        int total = 0;
        for (int i = 0; i <= 1000; i++) {
            total += path[i];
            if (total > capacity) {
                return false;
            }
        }
        return total <= capacity;
    }
}