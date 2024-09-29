# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkRight(self, root: Optional[TreeNode], val: int) -> bool:
        if not root:
            return True
        
        if root.val <= val:
            return False

        return self.checkRight(root.left, val) and self.checkRight(root.right, val)

    def checkLeft(self, root: Optional[TreeNode], val: int) -> bool:
        if not root:
            return True
        
        if root.val >= val:
            return False
            
        return self.checkLeft(root.left, val) and self.checkLeft(root.right, val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not self.checkLeft(root.left, root.val) or not self.checkRight(root.right, root.val):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)