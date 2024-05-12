from itertools import permutations
from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def score(perm: List[int]) -> int:
            ans = 0
            for i in range(len(perm)):
                if i == len(perm) - 1:
                    ans += abs(perm[i] - nums[perm[0]])
                else:
                    ans += abs(perm[i] - nums[perm[i+1]])
            return ans

        print(score([0, 1, 2, 3]))
        print(score([0, 2, 3, 1]))

        ret = [-1] * len(nums)
        ret[0] = 0

        for i in range(1, n):
            prev = ret[i-1]

            # last tc
            if i == n-1:
                for j in range(n):
                    if j not in ret:
                        ret[i] = j
                break

            min_add = 10**5+5
            index = -1

            for j in range(len(nums)):
                if j not in ret and abs(nums[j] - prev) < min_add:
                    min_add = abs(nums[j] - prev)
                    index = j
            ret[i] = index

        min_ans = score(ret)

        print(f'min_ans is {min_ans}')

        for perm in permutations(range(n)):
            if score(list(perm)) == min_ans:
                return list(perm)

s = Solution()

nums = [1,0,2]

# nums = [0,2,1]

# nums = [1, 0, 2, 3]

# nums = [1, 2, 0]

nums = [2, 1, 0]
# i put [0, 2, 1]
# should be [0, 1, 2]

nums = [0,2,1,3]
# i put [0, 1, 2, 3]
# should be [0, 2, 3, 1]

print(s.findPermutation(nums))
