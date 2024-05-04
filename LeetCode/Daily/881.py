# Sat, May 4, 2024

import bisect
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        ans = 0
        while people:
            if len(people) == 1:
                ans += 1
                break

            current = people[0]
            del people[0]
            index = bisect_right(people, limit - current)

            # print(f'{current} {index}')
            if index == 0:
                ans += 1
            else:
                del people[index-1]
                ans += 1
        
        return ans

s = Solution()

people = [1,2]
limit = 3

people = [3,2,2,1]
limit = 3

people = [3,5,3,4]
limit = 5

print(s.numRescueBoats(people, limit))