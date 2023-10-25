class Solution {
    public int punishmentNumber(int n) {
        int res = 0;
        for (int i = 1; i <= n; i++) {
            String s = Integer.toString(i * i);
            if (dfs(s, 0, 0, i)) {
                res += i * i;
            }
        }
        return res;
    }

    public boolean dfs(String s, int pos, int total, int target) {
        if (pos == s.length()) {
            return total == target;
        }
        int sum = 0;
        for (int i = pos; i < s.length(); i++) {
            sum = sum * 10 + s.charAt(i) - '0';
            if (sum + total > target) {
                break;
            } else if (dfs(s, i + 1, sum + total, target)) {
                return true;
            }
        }
        return false;
    }
}