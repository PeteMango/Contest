from typing import List

class binaryIndexTree:
    def __init__(self, size: int):
        self.n = size
        self.B1 = [0] * (size+1)
        self.B2 = [0] * (size+1)

    def increment(self, l, r: int):
        self.update(l, r, 1)

    def update(self, l, r, val: int):
        l, r = l + 1, r + 1

        self.add(self.B1, l, val)
        self.add(self.B1, r+1, -val)
        self.add(self.B2, l, val*(l-1))
        self.add(self.B2, r+1, -val*r)

    def add(self, a: List[int], idx, val: int) -> None:
        while idx <= self.n:
            a[idx] += val
            idx += idx & -idx

    def query(self, l, r: int) -> int:
        l, r = l + 1, r + 1

        return self.sum(r) - self.sum(l-1)

    def sum(self, idx: int) -> int:
        return self.sumOf(self.B1, idx) * idx - self.sumOf(self.B2, idx)

    def sumOf(self, a: List[int], idx: int) -> int:
        ans = 0
        while idx > 0:
            ans += a[idx]
            idx -= idx & -idx

        return ans

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        st = {}

        bit = binaryIndexTree(n)
        ans, dp = 0, 0

        for i in range(n):
            if nums[i] in st:
                l = st[nums[i]]
            else:
                l = -1

            dp = (dp + 2 * bit.query(l+1, i) + (i-l)) % MOD
            ans = (ans + dp) % MOD

            bit.increment(l+1, i)
            st[nums[i]] = i

        return ans

s = Solution()

nums = [1,2,1]

nums = [1,1]

print(s.sumCounts(nums))
