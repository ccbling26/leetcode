import java.util.Map;

class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = Map.of(
                'I', 1,
                'V', 5,
                'X', 10,
                'L', 50,
                'C', 100,
                'D', 500,
                'M', 1000);
        char pre = ' ';
        int res = 0;
        for (char c : s.toCharArray()) {
            res += map.get(c);
            if (c == 'I') {
            } else if (c == 'V' || c == 'X') {
                if (pre == 'I') {
                    res -= 2 * map.get('I');
                }
            } else if (c == 'L' || c == 'C') {
                if (pre == 'X') {
                    res -= 2 * map.get('X');
                }
            } else {
                if (pre == 'C') {
                    res -= 2 * map.get('C');
                }
            }
            pre = c;
        }
        return res;
    }
}