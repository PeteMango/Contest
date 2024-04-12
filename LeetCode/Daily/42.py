from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1] , height[i])

        right[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        water = 0

        for i in range(1, n-1):
            water += max(0, min(left[i-1], right[i+1]) - height[i])

        return water

s = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]

height = [4,2,0,3,2,5]

print(s.trap(height))
