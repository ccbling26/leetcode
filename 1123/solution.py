from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find(node):
            if not node:
                return 0, None
            l, n = find(node.left)
            r, m = find(node.right)
            if l > r:
                return l+1, n
            elif l < r:
                return r+1, m
            else:
                return l + 1, node
        return find(root)[1]
