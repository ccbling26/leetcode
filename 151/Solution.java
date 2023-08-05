class Solution {
    private char[] charList;

    public void reverse(int x, int y) {
        while (x < y) {
            char tmp = charList[x];
            charList[x] = charList[y];
            charList[y] = tmp;
            x++;
            y--;
        }
    }

    public String reverseWords(String s) {
        charList = s.toCharArray();
        reverse(0, charList.length - 1);
        int n = charList.length, x = 0, y = 0, l = 0;
        while (y < n) {
            if (charList[y] != ' ') {
                x = y;
                if (l != 0) {
                    charList[l] = ' ';
                    l++;
                }
                while (y < n && charList[y] != ' ') {
                    charList[l] = charList[y];
                    l++;
                    y++;
                }
                reverse(l - y + x, l - 1);
            }
            y++;
        }
        return String.valueOf(charList, 0, l);
    }
}
