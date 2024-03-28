from collections import deque

class Solution:
    def zez(self, s: str) -> bool:
        sk = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                sk.append(c)
            else:
                if len(sk) == 0:
                    return False
                if c == ']' and sk[-1] != '[':
                    return False
                if c == ')' and sk[-1] != '(':
                    return False
                if c == '}' and sk[-1] != '{':
                    return False
                sk.pop()

        return len(sk) == 0

s = Solution()

str = "()"

str = "()[]{}"

str = "(]"

print(s.isValid(str))
