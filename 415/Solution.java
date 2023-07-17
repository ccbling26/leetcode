class Solution {
    public String addStrings(String num1, String num2) {
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        StringBuffer ans = new StringBuffer();
        int add = 0;
        while (i >= 0 || j >= 0) {
            int val1 = i >= 0 ? num1.charAt(i) - '0': 0;
            int val2 = j >= 0 ? num2.charAt(j) - '0': 0;
            int total = add + val1 + val2;
            ans.append(total % 10);
            add = total / 10;
            i--;
            j--;
        }
        if (add > 0) {
            ans.append(add);
        }
        ans.reverse();
        return ans.toString();
    }
}