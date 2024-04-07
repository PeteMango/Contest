# Thu, April 4, 2024

from collections import deque

class Solution:
    def makeGood(self, s: str) -> str:
        sk = deque()

        for char in s:
            if sk and abs(ord(char) - ord(sk[-1])) == 32:
                sk.pop()
            else:
                sk.append(char)

        return ''.join(sk)

s = Solution()

str = "leEeetcode"

str = "abBAcC"

str = "s"

print(s.makeGood(str))
