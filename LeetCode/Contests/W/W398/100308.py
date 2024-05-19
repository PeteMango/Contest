from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            ret = [True] * len(queries)
            return ret

        special = [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i-1] % 2:
                special[i-1] = 1

        psa = [0] * (len(nums) - 1)
        psa[0] = special[0]
        for i in range(1, len(special)):
            psa[i] = psa[i-1] + special[i]

        ret = [False] * len(queries)
        for i in range(len(queries)):
            x, y = queries[i]
            if x == y:
                ret[i] = True
            elif x == 0:
                ret[i] = psa[y-1] == y-x
            else:
                ret[i] = psa[y-1] - psa[x-1] == y-x
        return ret


s = Solution()

nums = [3,4,1,2,6]
queries = [[0,4]]

# nums = [4,3,1,6]
# queries = [[0,2],[2,3]]

nums = [1]
queries = [[0, 0]]

nums = [3, 4]
queries = [[0, 0]]

print(s.isArraySpecial(nums, queries))
