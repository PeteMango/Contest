# Mon, April 8, 2024
# Total Solar Eclipse

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ret = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[i] == 0:
                    continue
                else:
                    tickets[i] -= 1
                    ret += 1

        return ret

s = Solution()

tickets = [2,3,2]
k = 2

tickets = [5,1,1,1]
k = 0

print(s.timeRequiredToBuy(tickets, k))
