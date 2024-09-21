class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n, mx = len(heights), 0
        l, r = 0, n-1
        while l < r:
            mx = max(mx, min(heights[r], heights[l]) * (r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return mx