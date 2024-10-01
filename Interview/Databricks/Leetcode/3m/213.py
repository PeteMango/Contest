class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def max_value(a: List[int]) -> int:
            n = len(a)
            if n == 0:
                return 0
            if n == 1:
                return a[0]

            dp = [0] * n
            dp[0] = a[0]
            dp[1] = max(a[0], a[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + a[i])

            return dp[-1]
        
        return max(max_value(nums[0:len(nums)-1]), max_value(nums[1:]))