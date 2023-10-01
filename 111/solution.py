from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def find(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = find(node.left)
            r = find(node.right)
            return 1 + min(l, r) if l != 0 and r != 0 else 1 + max(l, r)
        return find(root)
