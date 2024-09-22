class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k, h):
            req = 0
            for p in piles:
                req += p // k
                if p % k != 0:
                    req += 1
            return req <= h
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if canEat(mid, h):
                r = mid - 1
            else:
                l = mid + 1
        
        return l