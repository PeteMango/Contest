# Sat, April 27, 2024

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        
        def dp(i, j):
            if i == len(key):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = float('inf')
            for k in range(len(ring)):
                if ring[k] == key[i]:
                    diff = abs(j - k)
                    steps = min(diff, len(ring) - diff)
                    result = min(result, steps + dp(i + 1, k))
            
            memo[(i, j)] = result
            return result
        
        return dp(0, 0) + len(key)
        
s = Solution()

ring = "godding"
key = "gd"

ring = "godding"
key = "godding"

print(s.findRotateSteps(ring, key))