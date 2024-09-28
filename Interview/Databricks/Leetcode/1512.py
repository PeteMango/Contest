class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        ans = 0
        for k, v in d.items():
            ans += v * (v-1) // 2
        return ans