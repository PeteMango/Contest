from collections import defaultdict

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = defaultdict(int)

        for i in range(0, len(word), k):
            d[word[i:i+k]] += 1


        max_value = max(d.values())

        return len(word) // k - max_value

s = Solution()

word = "leetcodeleet"
k = 4

word = "leetcoleet"
k = 2

print(s.minimumOperationsToMakeKPeriodic(word, k))
