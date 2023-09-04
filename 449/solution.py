from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        arr = []

        def postOrder(node: Optional[TreeNode]):
            if not node:
                return
            postOrder(node.left)
            postOrder(node.right)
            arr.append(str(node.val))
        postOrder(root)
        return " ".join(arr)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        arr = list(map(int, data.split(" ")))

        def build(lower: int, upper: int) -> Optional[TreeNode]:
            if not arr or arr[-1] < lower or arr[0] > upper:
                return None
            val = arr.pop()
            node = TreeNode(val)
            node.right = build(val, upper)
            node.left = build(lower, val)
            return node
        return build(-inf, inf)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
