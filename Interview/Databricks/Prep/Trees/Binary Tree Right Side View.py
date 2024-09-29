# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import insort

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        pq = deque([(0, root)])
        ret = []

        while pq:
            h, node = pq.popleft()
            if len(ret) <= h:
                ret.append([node.val])
            else:
                ret[h].append(node.val)

            if node.left:
                insort(pq, (h+1, node.left), key=lambda a: a[0])
            
            if node.right:
                insort(pq, (h+1, node.right), key=lambda a: a[0])
            

        return ret

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        inorder = self.levelOrder(root)

        ret = []
        for l in inorder:
            ret.append(l[-1])
        
        return ret
