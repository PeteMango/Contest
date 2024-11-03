from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for s in stones:
            heappush(pq, -s)
        
        while len(pq) > 1:
            a, b = -heappop(pq), -heappop(pq)
            if a == b:
                continue
            heappush(pq, -(a-b))
        
        if not pq:
            return 0

        return -pq[0]