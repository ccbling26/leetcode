class Solution {
    public int subtractProductAndSum(int n) {
        int a = 1, b = 0;
        while (n > 0) {
            int c = n % 10;
            n /= 10;
            a *= c;
            b += c;
        }
        return a - b;
    }
}