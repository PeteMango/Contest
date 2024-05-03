# Tue, April 30, 2024

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans, curprefix = 0, 0
        count = [0] * 1024
        count[0] = 1

        for c in word:
            curprefix ^= 1 << (ord(c) - ord('a'))
            ans += count[curprefix]
            ans += sum(count[curprefix ^ 1 << j] for j in range(10))
            count[curprefix] += 1
        
        return ans

s = Solution()

word = "aba"

word = "aabb"

word = "he"

print(s.wonderfulSubstrings(word))