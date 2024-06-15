# Thu, June 6, 2024

from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        keys = sorted(freq.keys())

        for key in keys:
            if freq[key] > 0:
                start = freq[key]
                for i in range(key, key + groupSize):
                    if freq[i] < start:
                        return False
                    freq[i] -= start
        return True

s = Solution()

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

hand = [1,2,3,4,5]
groupSize = 4

print(s.isNStraightHand(hand, groupSize))
