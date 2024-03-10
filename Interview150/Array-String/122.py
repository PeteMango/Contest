from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_price, mx_profit = prices[0], 0

        for i, val in enumerate(prices):
            if i < 1:
                continue

            if val < current_price:
                current_price = val
            else:
                mx_profit += val - current_price
                current_price = val

        return mx_profit

s = Solution()

# prices = [7,1,5,3,6,4]

# prices = [1,2,3,4,5]

prices = [7,6,4,3,1]

print(s.maxProfit(prices))
