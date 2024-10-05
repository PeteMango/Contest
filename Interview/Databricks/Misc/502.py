from bisect import insort
from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        opt, cando = deque(), []
        for c, p in zip(capital, profits):
            if c <= w:
                heappush(cando, -p)
                continue
            
            opt.append((c, p))

        opt = deque(sorted(opt))

        profit = 0
        for i in range(k):
            if not cando:
                break
        
            gain = heappop(cando)
            profit -= gain

            while opt and opt[0][0] <= profit + w:
                heappush(cando, -opt[0][1])
                opt.popleft()

        return profit + w