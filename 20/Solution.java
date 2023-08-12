import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> relations = new HashMap<>();
        relations.put(')', '(');
        relations.put(']', '[');
        relations.put('}', '{');
        List<Character> queue = new ArrayList<>();
        HashSet<Character> needAdd = new HashSet<>();
        needAdd.add('(');
        needAdd.add('[');
        needAdd.add('{');
        for (char c : s.toCharArray()) {
            if (needAdd.contains(c)) {
                queue.add(c);
            } else if (queue.size() == 0) {
                return false;
            } else if (queue.get(queue.size() - 1) == relations.get(c)) {
                queue.remove(queue.size() - 1);
            } else {
                return false;
            }
        }
        return queue.size() == 0;
    }
}