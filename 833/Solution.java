import java.util.ArrayList;
import java.util.List;

class Solution {
    public String findReplaceString(String s, int[] indices, String[] sources, String[] targets) {
        int n = s.length();
        List<String> replaceItem = new ArrayList<>(n);
        List<Integer> replaceLength = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            replaceItem.add(i, Character.toString(s.charAt(i)));
            replaceLength.add(i, 1);
        }
        int m = indices.length;
        for (int i = 0; i < m; i++) {
            int indice = indices[i];
            String source = sources[i];
            String target = targets[i];
            if (s.startsWith(source, indice)) {
                replaceItem.set(indice, target);
                replaceLength.set(indice, source.length());
            }
        }
        StringBuilder res = new StringBuilder();
        int i = 0;
        while (i < n) {
            res.append(replaceItem.get(i));
            i += replaceLength.get(i);
        }
        return res.toString();
    }
}