import java.util.PriorityQueue;

class Solution {
    public int halveArray(int[] nums) {
        PriorityQueue<Double> queue = new PriorityQueue<Double>((a, b) -> {
            return b.compareTo(a);
        });
        double total = 0;
        int res = 0;
        for (int num : nums) {
            queue.add(Double.valueOf(num));
            total += num;
        }
        double count = 0;
        while (count < total / 2.0) {
            double num = queue.poll();
            num /= 2;
            count += num;
            res++;
            queue.add(num);
        
        }
        return res;
    }
}