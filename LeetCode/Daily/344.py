# Sun, June 2, 2024

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

s = Solution()

str = ["h","e","l","l","o"]

str = ["H","a","n","n","a","h"]

print(s.reverseString(str))
