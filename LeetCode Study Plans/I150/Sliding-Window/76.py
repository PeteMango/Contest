from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, mn = 0, 0, int(1e5 + 5)

        ret = ""

        dict = defaultdict(int)

        for c in t:
            dict[c] += 1

        seen = defaultdict(int)

        while r < len(s):
            if not self.isSubset(dict, seen):
                    seen[s[r]] += 1
                    r += 1

            while self.isSubset(dict, seen) and l < r:
                    if r - l < mn:
                        mn = r - l
                        ret = s[l:r]
                    seen[s[l]] -= 1
                    l += 1

        return ret

    def isSubset(self, dict, seen: defaultdict) -> bool:
        for key in dict:
            if dict[key] > seen[key]:
                return False

        return True

s = Solution()

# str = "ADOBECODEBANC"
# t = "ABC"

# str = "a"
# t = "a"

str = "a"
t = "aa"

print(s.minWindow(str, t))
