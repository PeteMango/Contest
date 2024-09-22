import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target) if bisect.bisect_left(nums, target) != bisect.bisect(nums, target) else -1