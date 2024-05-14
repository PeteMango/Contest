from typing import List, Optional
from collections import deque
from sortedcontainers import SortedList

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sl = SortedList()

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.sl = SortedList()
        self.traverse(root)

        ret = deque()
        sum = 0
        for i in range(k):
            ret.append(self.sl[i])
            sum += abs(self.sl[i] - target)

        for i in range(k, len(self.sl), 1):
            if abs(self.sl[i] - target) > abs(self.sl[i-k] - target):
                break

            ret.popleft()
            ret.append(self.sl[i])

        return list(ret)

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return

        self.sl.add(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
