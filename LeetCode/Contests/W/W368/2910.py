from typing import List
from collections import defaultdict

class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        d = defaultdict(int)
        for ball in balls:
            d[ball] += 1

        print(d)

        min_box = int(1e5 + 5)
        for key, val in d.items():
            min_box = min(min_box, val)
        
        new_min_box = min_box
        for key, val in d.items():
            if val > min_box + 1 and val // 2 < min_box:
                new_min_box = val // 2
        
        if new_min_box != min_box:
            return self.minBoxNeeded(d, new_min_box)
        else:
            return self.minBoxNeeded(d, min_box)

    def minBoxNeeded(self, d: defaultdict, min_box: int) -> int:
        box_needed = 0
        for key, val in d.items():
            if val <= min_box + 1:
                box_needed += 1
                continue
            if val % (min_box + 1) == 0:
                box_needed += val // (min_box + 1)
            else:
                box_needed += 1 + (val // (min_box + 1))
        return box_needed

s = Solution()

balls = [3,2,3,2,3]

balls = [10,10,10,3,1,1]

# balls = [1,1,3,3,1,1,2,2,3,1,3,2]
# 5
# 4
# 3

balls = [2,1,3,3,1,3,1,2,1,3,1,2,1,2,2]
    
print(s.minGroupsForValidAssignment(balls))
