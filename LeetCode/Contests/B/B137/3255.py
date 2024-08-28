class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[0]
        
        ans = []
        for i in range(k-1, len(nums)):
            if dp[i] >= k:
                ans.append(nums[i])
            else:
                ans.append(-1)
        
        return ans

s = Solution()

nums = [1,2,3,4,3,2,5]
k = 3

nums = [2,2,2,2,2]
k = 4

nums = [3,2,3,2,3,2]
k = 2

print(s.resultsArray(nums, k))