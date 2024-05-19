# Sun, May 19, 2024

from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        d = [(num^k) - num for num in nums]
        d.sort(reverse=True)

        ret = sum(nums)
        for i in range(0, len(nums)-1, 2):
            path = d[i] + d[i+1]
            if path <= 0:
                break

            ret += path

        return ret

s = Solution()

nums = [1,2,1]
k = 3
edges = [[0,1],[0,2]]

nums = [2,3]
k = 7
edges = [[0,1]]

nums = [7,7,7,7,7,7]
k = 3
edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]

print(s.maximumValueSum(nums, k, edges))
