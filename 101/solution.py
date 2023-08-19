from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root.left, root.right])
        while q:
            left = q.popleft()
            right = q.popleft()
            if left and not right or not left and right:
                return False
            elif not left and not right:
                continue
            elif left.val != right.val:
                return False
            else:
                q.extend([left.right, right.left, left.left, right.right])
        return True
