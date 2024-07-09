from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        cnt = 0
        for i in range(1, len(colors) - 1):
            if colors[i] != colors[i-1] and colors[i] != colors[i+1]:
                cnt += 1

        cnt += 1 if colors[0] != colors[1] and colors[0] != colors[-1] else 0
        cnt += 1 if colors[-1] != colors[-2] and colors[-1] != colors[0] else 0

        return cnt


s = Solution()

colors = [1, 1, 1]

colors = [0, 1, 0, 0, 1]

print(s.numberOfAlternatingGroups(colors))
