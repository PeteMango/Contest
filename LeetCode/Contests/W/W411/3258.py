class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def sum_substr(n: int) -> int:
            return n*(n+1)//2
        
        l, r = 0, 0
        nz, no = 0, 0
        ans = 0
        while r < len(s):
            if s[r] == '0':
                nz += 1
            else:
                no += 1

            while nz > k and no > k:
                if s[l] == '0':
                    nz -= 1
                else:
                    no -= 1
                l += 1
            
            ans += (r - l + 1)
            r += 1

        return ans

s = Solution()

str = "10101"
k = 1

str = "1010101"
k = 2

str = "11111"
k = 1

print(s.countKConstraintSubstrings(str, k))