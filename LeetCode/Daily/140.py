# Fri, May 24, 2024

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dp(i):
            result = [s[i:]] if s[i:] in wordDict else []
            for j in range(i+1, len(s)):
                if s[i:j] in wordDict:
                    for t in dp(j):
                        result.append(s[i:j]+' '+t)

            return result

        return dp(0)


s = Solution()

str = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

str = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

str = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(s.wordBreak(str, wordDict))
