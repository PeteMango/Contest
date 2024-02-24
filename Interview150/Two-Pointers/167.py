from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        return [-1, -1]



s = Solution()

# numbers = [2,7,11,15]
# target = 9

# numbers = [2,3,4]
# target = 6

# numbers = [-1,0]
# target = -1

numbers = [1,2,3,4,4,9,56,90]
target = 8

print(s.twoSum(numbers, target))
