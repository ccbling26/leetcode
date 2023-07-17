class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int res = 0;
        int[] counter = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n) {
                counter[n]++;
            } else {
                counter[citations[i]]++;
            }
        }
        for (int i = n; i >= 0; i--) {
            res += counter[i];
            if (res >= i) {
                return i;
            }
        }
        return 0;
    }
}