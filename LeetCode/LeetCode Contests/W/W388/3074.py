from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sum = 0
        for x in apple:
            sum += x

        capacity.sort(reverse=True)

        need, t = 0, 0
        for x in capacity:
            t += x
            need += 1

            if t >= sum:
                return need

        return need

s = Solution()

# apple = [1,3,2]
# capacity = [4,3,1,5,2]

apple = [5,5,5]
capacity = [2,4,2,7]

print(s.minimumBoxes(apple, capacity))
