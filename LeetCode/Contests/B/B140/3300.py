class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = 10**5+5
        for n in nums:
            sd = sum(int(c) for c in str(n))
        
            min_sum = min(min_sum, sd)
        
        return min_sum
