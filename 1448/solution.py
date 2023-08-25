from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        q = deque([(root, -10001)])
        while q:
            node, val = q.popleft()
            if node.val >= val:
                res += 1
                val = node.val
            if node.left:
                q.append((node.left, val))
            if node.right:
                q.append((node.right, val))
        return res
