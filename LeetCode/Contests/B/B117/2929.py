class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0

        ans = self.combination(n + 2)

        if n > limit:
            ans -= 3 * self.combination(n - limit + 1)

        if n - 2 >= 2 * limit:
            ans += 3 * self.combination(n - 2 * limit)

        return ans

    def combination(self, n: int) -> int:
        return int(n * (n - 1) / 2)

solution = Solution()

test_cases = [
    (5, 2),
    (3, 3),
]

for n, limit in test_cases:
    result = solution.distributeCandies(n, limit)
    print(result)
