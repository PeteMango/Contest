from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = defaultdict()

        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        i = 0

        for c in pattern:
            if c in map:
                i += 1
            else:
                map[c] = words[i]
                i += 1

        i, j = 0, 0
        while i < len(words):
            if j >= len(pattern):
                j = 0

            if map[pattern[j]] != words[i]:
                return False

            i += 1
            j += 1

        st = set()
        cnt = 0

        for key in map:
            st.add(map[key])
            cnt += 1

        if len(st) == cnt:
            return True

        return False


s = Solution()

# pattern = "abba"
# str = "dog cat cat dog"

# pattern = "abba"
# str = "dog cat cat fish"

# pattern = "aaaa"
# str = "dog cat cat dog"

# pattern = "abba"
# str = "dog dog dog dog"

pattern = "aaa"
str = "aa aa aa aa"

print(s.wordPattern(pattern, str))
