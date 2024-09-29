# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.height(root.left) + self.height(root.right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.diameter(root), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    