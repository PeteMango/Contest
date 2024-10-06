from heapq import heapify, heappop
class Solution:
    def maximumTotalSum(self, mh: List[int]) -> int:
        for i in range(len(mh)):
            mh[i] = -mh[i]
        
        heapify(mh)
        cur_max = -mh[0]
        ans = 0

        while mh:
            print(f'cur_max: {cur_max}')
            if cur_max == 0:
                return -1
            t_max = -heappop(mh)
            if t_max < cur_max:
                ans += t_max
                cur_max = t_max - 1 
            else:
                ans += cur_max
                cur_max -= 1
        
        return ans
        

