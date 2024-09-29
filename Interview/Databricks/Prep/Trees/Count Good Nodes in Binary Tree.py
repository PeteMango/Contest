# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countGood(self, root: TreeNode, max_so_far: int) -> int:
        if not root:
            return 0
        
        cnt = 0
        if root.val >= max_so_far:
            cnt += 1
        
        max_so_far = max(max_so_far, root.val)
        cnt += self.countGood(root.left, max_so_far) + self.countGood(root.right, max_so_far)
    
        return cnt

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        return self.countGood(root, -105)