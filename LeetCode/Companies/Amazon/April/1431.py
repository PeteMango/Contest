from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = -1
        for x in candies:
            mx = max(x, mx)

        ret = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mx:
                ret[i] = True

        return ret

s = Solution()

candies = [2,3,5,1,3]
extraCandies = 3

candies = [4,2,1,1,2]
extraCandies = 1

candies = [12,1,12]
extraCandies = 10

print(s.kidsWithCandies(candies, extraCandies))
