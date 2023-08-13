import java.util.HashMap;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> counter = new HashMap<>();
        for (char c : magazine.toCharArray()) {
            if (counter.containsKey(c)) {
                counter.put(c, counter.get(c) + 1);
            } else {
                counter.put(c, 1);
            }
        }
        for (char c : ransomNote.toCharArray()) {
            if (!counter.containsKey(c) || counter.get(c) == 0) {
                return false;
            }
            counter.put(c, counter.get(c) - 1);
        }
        return true;
    }
}