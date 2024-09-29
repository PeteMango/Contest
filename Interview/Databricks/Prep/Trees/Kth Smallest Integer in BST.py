# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getNodes(self, root: Optional[TreeNode], pq: List[int]):
        if not root:
            return
        
        heapq.heappush(pq, root.val)
        
        self.getNodes(root.left, pq)
        self.getNodes(root.right, pq)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []

        self.getNodes(root, pq)

        for i in range(k-1):
            heapq.heappop(pq)
        
        return pq[0]
