from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

s = Solution()

str = ["h","e","l","l","o"]

s.reverseString(str)

print(str)
