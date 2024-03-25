from typing import List

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        all_substrings = self.generateSubstrings(s)

        max_len = -1
        for str in all_substrings:
            if self.isGood(str):
                max_len = max(max_len, len(str))

        return max_len

    def isGood(self, s: str) -> bool:
        freq = {}

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for key, value in freq.items():
            if value > 2:
                return False

        return True

    def generateSubstrings(self, s: str) -> List[str]:
        substrings = []
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substrings.append(s[start:end])
        return substrings

s = Solution()

str = "bcbbbcba"

str = "aaaa"

print(s.maximumLengthSubstring(str))
