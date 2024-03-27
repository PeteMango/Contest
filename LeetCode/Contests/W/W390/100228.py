class Solution:
    def minOperations(self, k: int) -> int:
        # k = 11
        # [1]
        # [2]
        # [3]
        # [4]
        # [4, 4]
        # [4, 4, 4]
        #
        # k = 1
        # [1]
        #
        # k = 2
        # [1]
        # [1, 1]
        #
        # k = 3
        # [1]
        # [2]
        # [2, 2]
        #
        # k = 4
        # [1]
        # [2]
        # [2, 2]
        #
        # k = 5
        # [1]
        # [2]
        # [3]

        min_op = int(1e6 + 5)
        for i in range(1, k+1):
            a = (k // i) - 1 if k % i == 0 else (k // i)
            b = i - 1

            min_op = min(min_op, a+b)

        return min_op

s = Solution()

k = 11

k = 1

print(s.minOperations(k))
