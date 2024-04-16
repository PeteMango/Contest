# Mon, April 15, 2024

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    totalSum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalSum = 0
        self.computeSum(root=root, curNum="")
        return self.totalSum

    def computeSum(self, root: Optional[TreeNode], curNum: str) -> None:
        if root is None:
            return

        curNum += str(root.val)

        if self.isLeaf(root):
            self.totalSum += int(curNum)
            return

        self.computeSum(root.left, curNum)
        self.computeSum(root.right, curNum)


    def isLeaf(self, node: Optional[TreeNode]) -> bool:
        if node and node.left is None and node.right is None:
            return True

        return False
