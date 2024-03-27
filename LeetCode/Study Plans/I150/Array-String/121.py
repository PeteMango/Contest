from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_lowest, mx_profit = prices[0], 0

        for i, val in enumerate(prices):
            if i < 1:
                continue

            if val < current_lowest:
                current_lowest = val
            else:
                mx_profit = max(mx_profit, val - current_lowest)

        return mx_profit

s = Solution()

# prices = [7,1,5,3,6,4]

prices = [7,6,4,3,1]

print(s.maxProfit(prices))
