class Solution {
    public int countPoints(String rings) {
        int n = rings.length();
        int[] arr = new int[10];
        for (int i = 0; i < n; i += 2) {
            char color = rings.charAt(i);
            int idx = rings.charAt(i + 1) - '0';
            if (color == 'R') {
                arr[idx] |= 4;
            } else if (color == 'G') {
                arr[idx] |= 2;
            } else {
                arr[idx] |= 1;
            }
        }
        int res = 0;
        for (int i = 0; i < 10; i++) {
            if (arr[i] == 7) {
                res++;
            }
        }
        return res;
    }
}