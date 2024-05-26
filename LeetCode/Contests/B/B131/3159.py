from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indicies = []
        for i, num in enumerate(nums):
            if num == x:
                indicies.append(i)
        # print(indicies)
        ret = [0] * len(queries)
        for i, query in enumerate(queries):
            if query > len(indicies):
                ret[i] = -1
                continue
            ret[i] = indicies[query-1]

        return ret

s = Solution()

nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1

nums = [1,2,3]
queries = [10]
x = 5

print(s.occurrencesOfElement(nums, queries, x))
