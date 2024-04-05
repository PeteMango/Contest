# Wed, April 3, 2024

from collections import deque

class Solution:
    def maxDepth(self, s: str) -> int:
        sk = deque()
        mx_depth = 0

        for c in s:
            if c == ')':
                sk.pop()

            if c == '(':
                sk.append(c)

            mx_depth = max(mx_depth, len(sk))

        return mx_depth

s = Solution()

str = "(1+(2*3)+((8)/4))+1"

str = "(1)+((2))+(((3)))"

print(s.maxDepth(str))
