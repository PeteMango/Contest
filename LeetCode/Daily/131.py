# Tue, May 21, 2024

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []

        def isPalidrome(string: str) -> bool:
            return string == string[::-1]

        def dfs(start, path):
            if start == len(s):
                self.ans.append(path[:])
                return

            for j in range(start + 1, len(s) + 1):
                if isPalidrome(s[start:j]):
                    path.append(s[start:j])
                    dfs(j, path)
                    path.pop()

        dfs(0, [])
        return self.ans


s = Solution()

str = "aab"

str = "a"

print(s.partition(str))
