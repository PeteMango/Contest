# Tue, April 2, 2024

from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = defaultdict()

        for i in range(len(s)):
            if s[i] != t[i]:
                if s[i] in map and map[s[i]] != t[i]:
                    return False
                else:
                    map[s[i]] = t[i]
            else:
                if s[i] not in map:
                    map[s[i]] = t[i]
                if s[i] in map and map[s[i]] != t[i]:
                   return False

        st = set()
        cnt = 0

        for key in map:
            st.add(map[key])
            cnt += 1

        if len(st) != cnt:
            return False

        # print(st)
        print(map)

        return True

s = Solution()

str = "egg"
t = "add"

str = "foo"
t = "bar"

str = "paper"
t = "title"

print(s.isIsomorphic(str, t))
