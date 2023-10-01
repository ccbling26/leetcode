from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = False

        def find(node: Optional[TreeNode]) -> int:
            nonlocal flag
            if not node or flag:
                return 0
            l = find(node.left)
            r = find(node.right)
            if abs(l - r) > 1:
                flag = True
                return 0
            return 1 + max(l, r)
        find(root)
        return not flag
