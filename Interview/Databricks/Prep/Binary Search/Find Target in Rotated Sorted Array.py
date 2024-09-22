from bisect import bisect_left, bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1

        if l >= n:
            return bisect_left(nums, target) if bisect(nums, target) != bisect_left(nums, target) else -1
        elif bisect_left(nums, target, 0, l) != bisect(nums, target, 0, l):
            return bisect_left(nums, target, 0, l-1)
        elif bisect_left(nums, target, l, n) != bisect(nums, target, l, n):
            return bisect_left(nums, target, l, n-1)
        return -1