from bisect import insort, bisect, bisect_left

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n, min_diff, cur = len(nums), 10**9 + 7, []
        for i in range(x, n):
            insort(cur, nums[i-x])

            lidx, ridx = bisect_left(cur, nums[i]), bisect(cur, nums[i])

            # found equal
            if lidx != ridx:
                return 0
            
            # check less than
            if lidx > 0:
                min_diff = min(min_diff, abs(cur[lidx-1] - nums[i]))
            
            if ridx != len(cur):
                min_diff = min(min_diff, abs(cur[ridx] - nums[i]))
        
        return min_diff