# Sun, April 21, 2024

from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        vis = set(deadends)

        q = deque([(0, '0000')])

        def getChild(cur: str) -> List[str]:
            child = []

            for i in range(4):
                incr = cur[:i] + str((int(cur[i]) + 1) % 10) + cur[i+1:]
                decr = cur[:i] + str((int(cur[i]) - 1) % 10) + cur[i+1:]

                child.append(incr)
                child.append(decr)

            return child

        while q:
            ans, cur = q.popleft()

            if cur == target:
                return ans

            if cur in vis:
                continue

            vis.add(cur)

            for child in getChild(cur):
                if child not in vis:
                    q.append((ans+1, child))

        return -1

s = Solution()

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

deadends = ["8888"]
target = "0009"

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"

print(s.openLock(deadends, target))
