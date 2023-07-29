import java.util.ArrayList;
import java.util.List;

class Solution {
    public long[] handleQuery(int[] nums1, int[] nums2, int[][] queries) {
        SegTree segTree = new SegTree(nums1);
        int n = nums1.length;
        long total = 0;
        for (int num : nums2) {
            total += num;
        }
        List<Long> tmp = new ArrayList<>();
        for (int[] query : queries) {
            int x = query[0], y = query[1], z = query[2];
            if (x == 1) {
                segTree.ReverseRange(y, z);
            } else if (x == 2) {
                total += segTree.SumRange(0, n - 1) * y;
            } else {
                tmp.add(total);
            }
        }
        long[] ans = new long[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            ans[i] = tmp.get(i);
        }
        return ans;
    }
}

class SegNode {
    private int left, right;
    private long total;
    private boolean lazyTag;

    public SegNode() {
        left = 0;
        right = 0;
        total = 0;
        lazyTag = false;
    }

    public int GetLeft() {
        return left;
    }

    public void SetLeft(int left) {
        this.left = left;
    }

    public int GetRight() {
        return right;
    }

    public void SetRight(int right) {
        this.right = right;

    }

    public long GetTotal() {
        return total;
    }

    public void UpdateTotal() {
        total = right - left + 1 - total;
    }

    public void SetTotal(long total) {
        this.total = total;
    }

    public boolean GetLazyTag() {
        return lazyTag;
    }

    public void SetLazyTag(boolean lazyTag) {
        this.lazyTag = lazyTag;
    }

    public void ReverseLazyTag() {
        lazyTag = !lazyTag;
    }
}

class SegTree {
    private int[] nums;
    private SegNode[] arr;

    public SegTree(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        arr = new SegNode[4 * n + 1];
        for (int i = 0; i < 4 * n + 1; i++) {
            arr[i] = new SegNode();
        }
        build(1, 0, n - 1);
    }

    public void build(int idx, int l, int r) {
        arr[idx].SetLeft(l);
        arr[idx].SetRight(r);
        if (l == r) {
            arr[idx].SetTotal(nums[l]);
            return;
        }
        int mid = (l + r) / 2;
        build(2 * idx, l, mid);
        build(2 * idx + 1, mid + 1, r);
        arr[idx].SetTotal(arr[2 * idx].GetTotal() + arr[2 * idx + 1].GetTotal());
    }

    public void ReverseRange(int l, int r) {
        Modify(1, l, r);
    }

    public long SumRange(int l, int r) {
        return Query(1, l, r);
    }

    public long Query(int idx, int l, int r) {
        if (arr[idx].GetLeft() > r || arr[idx].GetRight() < l) {
            return 0;
        }
        if (arr[idx].GetLeft() <= l && arr[idx].GetRight() >= r) {
            return arr[idx].GetTotal();
        }
        Pushdown(idx);
        long res = 0;
        if (arr[2 * idx].GetRight() >= l) {
            res += Query(2 * idx, l, r);
        }
        if (arr[2 * idx + 1].GetLeft() <= r) {
            res += Query(2 * idx + 1, l, r);
        }
        return res;
    }

    public void Modify(int idx, int l, int r) {
        if (arr[idx].GetLeft() >= l && arr[idx].GetRight() <= r) {
            arr[idx].UpdateTotal();
            arr[idx].ReverseLazyTag();
            return;
        }
        Pushdown(idx);
        if (arr[2 * idx].GetRight() >= l) {
            Modify(2 * idx, l, r);
        }
        if (arr[2 * idx + 1].GetLeft() <= r) {
            Modify(2 * idx + 1, l, r);
        }
        arr[idx].SetTotal(arr[2 * idx].GetTotal() + arr[2 * idx + 1].GetTotal());
    }

    public void Pushdown(int idx) {
        if (arr[idx].GetLazyTag() == true) {
            arr[2 * idx].ReverseLazyTag();
            arr[2 * idx + 1].ReverseLazyTag();
            arr[2 * idx].UpdateTotal();
            arr[2 * idx + 1].UpdateTotal();
            arr[idx].SetLazyTag(false);
        }
    }
}