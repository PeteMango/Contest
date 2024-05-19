# Sat, May 18, 2024

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def excess(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = excess(node.left)
            right = excess(node.right)

            self.moves += abs(left) + abs(right)

            return node.val + left + right - 1

        excess(root)
        return self.moves
