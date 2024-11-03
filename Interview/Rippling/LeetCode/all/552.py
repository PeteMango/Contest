class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(100)
        def generate(absent: int, late: int, cur: int) -> int:
            if cur == n:
                return 1

            ans = generate(absent, 0, cur+1)        
            if absent < 1:
                ans += generate(absent + 1, 0, cur+1)
            if late < 2:
                ans += generate(absent, late+1, cur+1)
            

            return ans % MOD
        
        return generate(0, 0, 0) % MOD
