class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            print(nums[mid])
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1

        return nums[l] if l < len(nums) else nums[0]