import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []

        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))
        
        for i in range(k):
            val, idx = heapq.heappop(pq)
            heapq.heappush(pq, (val*multiplier, idx))
        
        ans = [0] * len(nums)
        for val, key in pq:
            ans[key] = val
        
        return ans
    
s = Solution()

nums = [2,1,3,5,6]
k = 5
multiplier = 2

nums = [1,2]
k = 3
multiplier = 4

print(s.getFinalState(nums, k, multiplier))