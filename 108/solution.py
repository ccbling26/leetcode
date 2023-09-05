from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def generate(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            elif left == right:
                return TreeNode(nums[left])
            mid = (right + left) // 2
            return TreeNode(
                val=nums[mid],
                left=generate(left, mid - 1),
                right=generate(mid + 1, right),
            )
        return generate(0, len(nums) - 1)
