from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        self.solve(target, candidates, [], ans)

        for i in range(len(ans)):
            ans[i].sort()

        unique_lists = []
        for sublist in ans:
            if sublist not in unique_lists:
                unique_lists.append(sublist)

        return unique_lists

    def solve(self, remain: int, candidates, current: List[int], ans: List[List[int]]):
        if remain == 0:
            ans.append(list(current))
            return

        if remain < 0:
            return

        for num in candidates:
            current.append(num)
            self.solve(remain - num, candidates, current, ans)
            current.pop()

        return

s = Solution()

candidates = [2,3,6,7]
target = 7

candidates = [2,3,5]
target = 8

candidates = [2]
target = 1

print(s.combinationSum(candidates, target))
