from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    move = 0

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.move += abs(left) + abs(right)
        return left + right + root.val - 1

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.move