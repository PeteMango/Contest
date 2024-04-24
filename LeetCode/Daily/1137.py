# Tue, April 23, 2024

class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]
        if n <= 2:
            return ans[n]

        for i in range(3, n+3):
            ans.append(ans[-1]+ans[-2]+ans[-3])

        # print(ans)
        return ans[n]

s = Solution()

n = 4

n = 25

print(s.tribonacci(n))
