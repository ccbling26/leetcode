from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def find(node: Optional[TreeNode]) -> int:
            if not node:
                return 0, 0
            l1, l2 = find(node.left)
            r1, r2 = find(node.right)
            c1 = node.val + l2 + r2
            c2 = max(l1, l2) + max(r1, r2)
            return c1, c2

        return max(find(root))
