class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasOccured = set()

        l, r, n, mx = 0, 0, len(s), 1

        if n == 0:
            return 0

        while l <= r and r < n:
            print(f'{l} - {r}')
            if s[r] in hasOccured:
                mx = max(mx, r - l)

                while s[r] in hasOccured:
                    hasOccured.remove(s[l])
                    l += 1
            else:
                hasOccured.add(s[r])
                r += 1

        mx = max(mx, r - l)

        return mx

s = Solution()

# str = "abcabcbb"

# str = "bbbbb"

# str = "pwwkew"

str = "au"

print(s.lengthOfLongestSubstring(str))
