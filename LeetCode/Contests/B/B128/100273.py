from typing import List
from math import log2
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        def build(nums: List[int], n: int) -> List[List[int]]:
            max_log = int(log2(n)) + 1
            sparse = [[0] * max_log for _ in range(n)]
            for i in range(n):
                sparse[i][0] = nums[i]
            j = 1
            while (1 << j) <= n:
                i = 0
                while (i + (1 << j) - 1) < n:
                    sparse[i][j] = max(sparse[i][j - 1], sparse[i + (1 << (j - 1))][j - 1])
                    i += 1
                j += 1

            return sparse

        def query(sparse: List[List[int]], l: int, r: int) -> int:
            j = int(log2(r - l + 1))
            return max(sparse[l][j], sparse[r - (1 << j) + 1][j])

        q = build(nums, n)
        d = defaultdict(list)
        for i, val in enumerate(nums):
            d[val].append(i)

        ans = 0
        for num, lst in d.items():
            i = 1
            ans += len(lst)
            while i < len(lst):
                t_idx = i
                while i < len(lst) and query(q, lst[i - 1], lst[i]) == num:
                    i += 1

                length = i - t_idx
                ans += (length + 1) * length // 2

                i += 1


        return ans

s = Solution()

nums = [1,4,3,3,2]

nums = [3,3,3]

nums = [1]

nums = [62,17,84,46,62]

nums = [148,147,148,150,149,146,147,147,148,148]

print(s.numberOfSubarrays(nums))
