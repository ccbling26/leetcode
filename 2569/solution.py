from typing import List


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        seg_tree = SegTree(nums1)
        total = sum(nums2)
        ans = []
        for x, y, z in queries:
            if x == 1:
                seg_tree.reverse_range(y, z)
            elif x == 2:
                total += seg_tree.sum_range(0, n - 1) * y
            else:
                ans.append(total)
        return ans


class SegNode:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.total = 0
        # 下传懒标记，即将当前区间的修改情况下传到其左右孩子结点
        self.lazy_tag = False


class SegTree:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        n = len(nums)
        self.arr = [SegNode() for _ in range(4 * n + 1)]
        self.build(1, 0, n - 1)

    def build(self, idx: int, l: int, r: int):
        obj = self.arr[idx]
        obj.l = l
        obj.r = r
        if l == r:
            obj.total = self.nums[l]
            return
        mid = (l + r) // 2
        self.build(idx * 2, l, mid)
        self.build(idx * 2 + 1, mid + 1, r)
        self.arr[idx].total = self.arr[idx * 2].total + \
            self.arr[idx * 2 + 1].total

    def sum_range(self, l: int, r: int) -> int:
        return self.query(1, l, r)

    def reverse_range(self, l: int, r: int):
        self.modify(1, l, r)

    def modify(self, idx: int, l: int, r: int):
        obj = self.arr[idx]
        if obj.l >= l and obj.r <= r:
            obj.total = obj.r - obj.l + 1 - obj.total
            obj.lazy_tag = not obj.lazy_tag
            return
        self.pushdown(idx)
        if self.arr[idx * 2].r >= l:
            self.modify(2 * idx, l, r)
        if self.arr[idx * 2 + 1].l <= r:
            self.modify(2 * idx + 1, l, r)
        obj.total = self.arr[idx*2].total + self.arr[idx * 2 + 1].total

    def pushdown(self, idx: int):
        obj = self.arr[idx]
        if obj.lazy_tag:
            l_obj = self.arr[idx * 2]
            r_obj = self.arr[idx * 2 + 1]
            l_obj.lazy_tag = not l_obj.lazy_tag
            r_obj.lazy_tag = not r_obj.lazy_tag
            l_obj.total = l_obj.r - l_obj.l + 1 - l_obj.total
            r_obj.total = r_obj.r - r_obj.l + 1 - r_obj.total
            obj.lazy_tag = False

    def query(self, idx: int, l: int, r: int) -> int:
        obj = self.arr[idx]
        if obj.l >= l and obj.r <= r:
            return obj.total
        if obj.l > r or obj.r < l:
            return 0
        self.pushdown(idx)
        res = 0
        if self.arr[2 * idx].r >= l:
            res += self.query(2 * idx, l, r)
        if self.arr[2 * idx + 1].l <= r:
            res += self.query(2 * idx + 1, l, r)
        return res
