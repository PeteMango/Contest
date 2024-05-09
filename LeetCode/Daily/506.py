# Wed, May 8, 2024

import heapq
from heapq import heappush, heappop
from typing import List
from bisect import bisect_left

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lenScore = len(score)
        answer = [0] * lenScore
        maxHeap = []
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for index, s in enumerate(score):
            heappush(maxHeap, (-s, index))

        number = 1
        while maxHeap:
            s, index = heappop(maxHeap)
            if number < 4:
                answer[index] = rank[number - 1]
            else:
                answer[index] = str(number)
            number += 1
        return answer

s = Solution()

score = [5,4,3,2,1]

score = [10,3,8,9,4]

print(s.findRelativeRanks(score))
