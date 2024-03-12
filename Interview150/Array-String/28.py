class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        return haystack.find(needle)

s = Solution()

haystack = "sadbutsad"
needle = "sad"

haystack = "leetcode"
needle = "leeto"

print(s.strStr(haystack, needle))
