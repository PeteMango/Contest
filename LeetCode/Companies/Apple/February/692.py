from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)

        for word in words:
            d[word] += 1

        ret = []

        sorted_lst = sorted(d.items(), key=lambda item: (-item[1], item[0]))

        for i in range(k):
            ret.append(sorted_lst[i][0])

        return ret

s = Solution()

words = ["i","love","leetcode","i","love","coding"]
k = 2

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4

words = ["i","love","leetcode","i","love","coding"]
k = 3

print(s.topKFrequent(words, k))
