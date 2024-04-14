# Sun, April 14, 2024

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        sum = 0
        if root.left is not None and self.isLeaf(root.left):
            sum += root.left.val
        else:
            sum += self.sumOfLeftLeaves(root.left)

        sum += self.sumOfLeftLeaves(root.right)
        return sum

    def isLeaf(self, node: Optional[TreeNode]) -> bool:
        return node.left is None and node.right is None
