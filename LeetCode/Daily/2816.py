# Tue, May 7, 2024

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(t: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = t

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        head = reverseList(head)

        carry = 0
        current = head
        while current:
            result = 2 * current.val + carry
            current.val = result % 10
            carry = result // 10
            prev = current
            current = current.next

        if carry:
            prev.next = ListNode(carry)

        head = reverseList(head)
        return head
