# Mon, June 10, 2024

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()

        ret = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ret += 1
        return ret

s = Solution()

heights = [1,1,4,2,1,3]

heights = [5,1,2,3,4]

heights = [1,2,3,4,5]

print(s.heightChecker(heights))
