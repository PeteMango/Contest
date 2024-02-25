from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in s:
            s_map[c] += 1

        for c in t:
            t_map[c] += 1

        for key in s_map:
            if s_map[key] != t_map[key]:
                return False

        return True

s = Solution()

# str = "anagram"
# t = "nagaram"

str = "rat"
t = "car"

print(s.isAnagram(str, t))
