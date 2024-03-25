from typing import List
from sortedcontainers import SortedList

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = SortedList()

        for val in citations:
            arr.add(val)

        h_index = 0
        for i in range(1005):
            num_more = len(citations) - arr.bisect_right(i-1)

            if num_more >= i:
                h_index = i

        return h_index

s = Solution()

# citations = [3,0,6,1,5]

citations = [1,3,1]

print(s.hIndex(citations))
