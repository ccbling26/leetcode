from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def get(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return
            res.append(node.val)
            get(node.left)
            get(node.right)
        get(root)
        return res
