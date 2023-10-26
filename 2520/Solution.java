import java.util.HashMap;

class Solution {
    public int countDigits(int num) {
        int res = 0;
        HashMap<Integer, Integer> counter = new HashMap<>();
        int tmp = num;
        while (tmp != 0) {
            int key = tmp % 10;
            if (counter.containsKey(key)) {
                counter.put(key, counter.get(key) + 1);
            } else {
                counter.put(key, 1);
            }
            tmp /= 10;
        }
        for (int key : counter.keySet()) {
            if (key != 0 && num % key == 0) {
                res += counter.get(key);
            }
        }
        return res;
    }
}