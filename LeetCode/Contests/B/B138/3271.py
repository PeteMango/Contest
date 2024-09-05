class Solution:
    def stringHash(self, s: str, k: int) -> str:
        def process(substr: str) -> str:
            print(substr)
            sum = 0
            for c in substr:
                sum += ord(c) - ord('a')
            
            sum = sum % 26
            return chr(sum + ord('a'))

        n = len(s)
        ans = ""
        for i in range(n//k):
            substr = s[i*k:i*k+k]
            ans += process(substr)

        return ans

s = Solution()

str = "abcd"
k = 2

str = "mxz"
k = 3

print(s.stringHash(str, k))