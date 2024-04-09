from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        num_min, num_max = int(1e9 + 5), 0
        for num in nums:
            num_min = min(num_min, num)
            num_max = max(num_max, num)

        l, r = num_min, num_max
        while l <= r:
            mid = (l + r) // 2

            tmp = nums.copy()

            val = self.solve(tmp, mid)

            print(f'mid: {mid} and val: {val}')

            if val <= mid:
                r = mid - 1
            else:
                l = mid + 1

        return l

    def solve(self, nums: List[int], target: int) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= target:
                continue
            else:
                diff = nums[i] - target
                nums[i-1] += diff
                nums[i] = target

        return nums[0]

s = Solution()

nums = [3,7,1,6]

nums = [10,1]

print(s.minimizeArrayValue(nums))
