import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> removeComments(String[] source) {
        List<String> res = new ArrayList<String>();
        List<Character> newLine = new ArrayList<Character>();
        boolean isBlock = false;
        for (String item : source) {
            int i = 0;
            int n = item.length();
            while (i < n) {
                if (isBlock) {
                    if (i + 1 < n && item.charAt(i) == '*' && item.charAt(i + 1) == '/') {
                        isBlock = false;
                        i++;
                    }
                } else {
                    if (i + 1 < n && item.charAt(i) == '/' && item.charAt(i + 1) == '*') {
                        isBlock = true;
                        i++;
                    } else if (i + 1 < n && item.charAt(i) == '/' && item.charAt(i + 1) == '/') {
                        break;
                    } else {
                        newLine.add(item.charAt(i));
                    }
                }
                i++;
            }
            if (isBlock == false && newLine.size() > 0) {
                char[] characters = new char[newLine.size()];
                for (int j = 0; j < newLine.size();j++) {
                    characters[j] = newLine.get(j).charValue();
                }
                res.add(new String(characters));
                newLine = new ArrayList<Character>();
            }
        }
        return res;
    }
}
