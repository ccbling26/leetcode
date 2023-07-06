import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Long> maximumEvenSplit(long finalSum) {
        List<Long> res = new ArrayList<>();
        if (finalSum % 2 == 1) {
            return res;
        }
        long i = 2;
        while (i <= finalSum) {
            res.add(i);
            finalSum -= i;
            i += 2;
        }
        res.set(res.size() - 1, res.get(res.size() - 1) + finalSum);
        return res;
    }
}
