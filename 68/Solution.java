import java.util.ArrayList;
import java.util.List;

class Solution {
    private String[] words;

    public List<String> fullJustify(String[] words, int maxWidth) {
        this.words = words;
        List<String> res  =new ArrayList<>();
        int i = 0, n = words.length;
        while (i < n) {
            int left = i, l = 0;
            while (i < n && l + words[i].length() + i - left <= maxWidth) {
                l += words[i].length();
                i++;
            }
            int blankCount = maxWidth - l;
            if (i == n) {
                res.add(join(left, i - 1, " ") + blank(blankCount - i + left + 1));
                break;
            }
            int count = i - left;
            if (count == 1) {
                res.add(words[left] + blank(blankCount));
            } else {
                int avg = blankCount / (count - 1);
                int more = blankCount % (count - 1);
                StringBuilder item = new StringBuilder();
                for (int j = 0; j < more;j++) {
                    item.append(words[left + j]);
                    item.append(blank(avg + 1));
                }
                item.append(join(left + more, i - 1, blank(avg)));
                res.add(item.toString());
            }
        }
        return res;
    }

    public String blank(int n) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < n; i++) {
            res.append(' ');
        }
        return res.toString();
    }

    public String join(int f, int t, String seq) {
        StringBuilder res = new StringBuilder();
        while (f < t) {
            res.append(words[f]);
            res.append(seq);
            f++;
        }
        res.append(words[f]);
        return res.toString();
    }
}