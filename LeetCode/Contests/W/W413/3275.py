from heapq import heappush, heappop

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        pq = []
        ret = []

        for q in queries:
            x, y = q
            heappush(pq, -(abs(x)+abs(y)))

            if k > len(pq):
                ret.append(-1)
                continue
            
            while len(pq) > k:
                heappop(pq)

            ret.append(-pq[0])
        
        return ret
    
s = Solution()

queries = [[1,2],[3,4],[2,3],[-3,0]]
k = 2

queries = [[5,5],[4,4],[3,3]]
k = 1

print(s.resultsArray(queries, k))