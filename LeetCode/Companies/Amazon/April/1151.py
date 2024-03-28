from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_ones = 0
        for x in data:
            if x == 1:
                num_ones += 1

        if num_ones == 1:
            return 0

        cur_ones = 0
        for i in range(num_ones):
            if data[i] == 1:
                cur_ones += 1

        mx_ones = cur_ones

        i = num_ones
        while i < len(data):
            cur_ones += data[i] - data[i - num_ones]

            mx_ones = max(mx_ones, cur_ones)
            i += 1

        return num_ones - mx_ones

s = Solution()

data = [1,0,1,0,1]

data = [0,0,0,1,0]

data = [1,0,1,0,1,0,0,1,1,0,1]

print(s.minSwaps(data))
