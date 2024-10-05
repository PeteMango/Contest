# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -10**5-5
    mindiff = 10**5 + 5

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.traverse(root.left)
        self.mindiff = min(self.mindiff, abs(root.val - self.prev))
        self.prev = root.val

        self.traverse(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        self.mindiff = 10**5 + 5

        self.traverse(root)
        return self.mindiff