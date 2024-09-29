# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inSubtree(self, root: Optional[TreeNode], val: int) -> bool:
        if not root:
            return False
        
        if root.val == val:
            return True
        
        return self.inSubtree(root.left, val) or self.inSubtree(root.right, val)

    def containsBoth(self, root: Optional[TreeNode], a, b: int) -> bool:
        return self.inSubtree(root, a) and self.inSubtree(root, b)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        
        a, b = p.val, q.val
        while True:
            if self.containsBoth(root.left, a, b):
                root = root.left
            elif self.containsBoth(root.right, a, b):
                root = root.right
            else:
                break
                
        return root
        
