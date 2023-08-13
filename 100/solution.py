from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if q and p:
            if q.val != p.val:
                return False
            if not self.isSameTree(p.left, q.left):
                return False
            return self.isSameTree(p.right, q.right)
        return False
