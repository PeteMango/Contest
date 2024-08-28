from collections import defaultdict

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        d = defaultdict(int)

        for i in range(len(s)):
            for j in range(1,len(s)-i+1):
                if s[i:i+j] == "":
                    continue
                d[s[i:i+j]] += 1
                # print(s[i:i+j])
    
        mx_len = 0
        for k, v in d.items():
            if v > 1:
                mx_len = max(mx_len, len(k))
        
        return mx_len

s = Solution()

str = "abcd"

str = "abbaba"

str = "aabcaabdaab"

print(s.longestRepeatingSubstring(str))
