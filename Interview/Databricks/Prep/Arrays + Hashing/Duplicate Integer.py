class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
            if d[n] > 1:
                return True
        return False