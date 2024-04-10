# Tue, April 9, 2024

from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque()

        dq.append(deck[len(deck) - 1])
        for i in range(len(deck) - 2, -1, -1):
            dq.appendleft(dq.pop())
            dq.appendleft(deck[i])

        ret = []
        while dq:
            ret.append(dq.popleft())

        return ret
