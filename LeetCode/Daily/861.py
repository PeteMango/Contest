# Mon, May 13, 2024

class Solution(object):
    def matrixScore(self, a):
        n = len(a)
        m = len(a[0])
        res = (1 << (m - 1)) * n

        for i in range(1, m):
            curr = 0
            for j in range(n):
                if a[j][i] == a[j][0]:
                    curr += 1
            res += (1 << (m - i - 1)) * max(curr, n - curr)

        return res

s = Solution()

grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]

grid = [[0]]

print(s.matrixScore(grid))
