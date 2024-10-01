# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        d = defaultdict(list)
        leaf = set()

        def buildGraph(root: Optional[TreeNode]) -> int:
            if not root:
                return
            
            if not root.left and not root.right:
                leaf.add(root.val)

            if root.left:
                d[root.left.val].append(root.val)
                d[root.val].append(root.left.val)
            
            if root.right:
                d[root.right.val].append(root.val)
                d[root.val].append(root.right.val)
            
            buildGraph(root.left)
            buildGraph(root.right)
        
        buildGraph(root)
        
        dq = deque()
        dq.append(k)
        dist = [1005] * 1005
        dist[k] = 1
        while dq:
            front = dq.popleft()
            for neighbor in d[front]:
                if dist[neighbor] < 1005:
                    # been updated
                    continue
                dist[neighbor] = dist[front] + 1
                dq.append(neighbor)
        
        min_ans, min_node = 1005, -1
        for k in leaf:
            if dist[k] < min_ans:
                min_ans = dist[k]
                min_node = k

        return min_node