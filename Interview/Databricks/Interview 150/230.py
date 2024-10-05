# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + self.count(root.left) + self.count(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        left = self.count(root.left)
        if left >= k:
            return self.kthSmallest(root.left, k)
        elif left+1 == k:
            return root.val
        return self.kthSmallest(root.right, k-left-1)