from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        while head.next is not None:
            head.val = int(1e5 + 5)
            if head.next.val == int(1e5 + 5):
                return True

            head = head.next

        return False

s = Solution()
