class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        l_max, r_max = height[0], height[r]

        ans = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                ans += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
        return ans