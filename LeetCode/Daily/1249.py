# Fri, April 5, 2024

from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        dq = deque()

        ret = ''
        for c in s:
            if c == '(':
                dq.append(c)
                ret += c
            elif c == ')' and len(dq) == 0:
                continue
            elif c == ')' and len(dq) > 0:
                dq.pop()
                ret += c
            else:
                ret += c

        to_remove = len(dq)
        cnt = 0
        final = ''

        if len(dq) == 0:
            return ret

        for i in range(len(ret) - 1, -1, -1):
            if ret[i] == '(' and cnt < to_remove:
                cnt += 1
                continue

            final = ret[i] + final

        return final

s = Solution()

str = "lee(t(c)o)de)"

str = "a)b(c)d"

str = "))(("

print(s.minRemoveToMakeValid(str))
