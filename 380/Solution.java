import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

class RandomizedSet {
    private List<Integer> nums;
    private HashMap<Integer, Integer> data;

    public RandomizedSet() {
        nums = new ArrayList<>();
        data = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (data.containsKey(val))
            return false;
        data.put(val, nums.size());
        nums.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!data.containsKey(val))
            return false;
        int delIdx = data.get(val);
        int lastIdx = nums.size() - 1;
        nums.set(delIdx, nums.get(lastIdx));
        data.put(nums.get(lastIdx), delIdx);
        nums.remove(lastIdx);
        data.remove(val);
        return true;
    }
    
    public int getRandom() {
        int idx = new Random().nextInt(nums.size());
        return nums.get(idx);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */