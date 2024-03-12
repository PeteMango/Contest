from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                if dp[i] <= dp[i-1]:
                    dp[i] = dp[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if dp[i] <= dp[i+1]:
                    dp[i] = dp[i+1] + 1

        print(dp)

        cookies_needed = 0
        for val in dp:
            cookies_needed += val

        return cookies_needed

s = Solution()

# ratings = [1,0,2]

ratings = [1,2,2]

print(s.candy(ratings))
