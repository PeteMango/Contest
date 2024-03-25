from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, mx = 0, len(height) - 1, -1

        while l < r:
            mx = max(mx, int((r - l) * min(height[l], height[r])))

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return mx

s = Solution()

# height = [1,8,6,2,5,4,8,3,7]

height = [1,1]

print(s.maxArea(height))
