# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root: Optional[TreeNode], l, r: int) -> bool:
        if not root:
            return True
        
        if root.val < l or root.val > r:
            return False
        
        return self.check(root.left, l, root.val-1) and self.check(root.right, root.val+1, r)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # i stole this solution, very elegant
        return self.check(root, -10**16-7, 10**16+7)
        