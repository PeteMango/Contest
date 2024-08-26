class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        mx = max(nums)
        mod = 10**9 + 7

        if multiplier == 1:
            return nums

        for i, num in enumerate(nums):
            heapq.heappush(pq, [num, i])
        
        while pq[0][0] * multiplier <= mx and k > 0:
            k -= 1
            num, idx = heapq.heappop(pq)
            new_num = num * multiplier

            mx = max(mx, new_num)
            heapq.heappush(pq, [new_num, idx])

        ans = [0] * len(nums)
        if k == 0:
            for val, key in pq:
                ans[key] = val
            return ans

        multiply_each = k // len(pq)
        multiply_left = k % len(pq)

        values = sorted(pq)

        for i in range(len(pq)):
            values[i][0] = values[i][0] * pow(multiplier, multiply_each, mod) % mod
        
        
        for i in range(multiply_left):
            values[i][0] = values[i][0] * multiplier % mod
        
        for val, key in pq:
            ans[key] = val
        
        return ans
    
s = Solution()

nums = [2,1,3,5,6]
k = 5
multiplier = 2

nums = [100000,2000]
k = 2
multiplier = 1000000

print(s.getFinalState(nums, k, multiplier))