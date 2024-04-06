# Sat, Feb 23, 2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        r = slow.next
        slow.next = None

        prev = None
        cur = r

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        r = prev

        l = head
        while r:
            nextl = l.next
            nextr = r.next

            l.next = r
            r.next = nextl

            l = nextl
            r = nextr
