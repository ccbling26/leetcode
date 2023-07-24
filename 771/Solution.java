import java.util.HashSet;

class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashSet<Character> hashSet = new HashSet<>();
        for (int i = 0; i < jewels.length(); i++) {
            hashSet.add(jewels.charAt(i));
        }
        int res = 0;
        for (int i = 0; i < stones.length(); i++) {
            if (hashSet.contains(stones.charAt(i))) {
                res++;
            }
        }
        return res;
    }
}