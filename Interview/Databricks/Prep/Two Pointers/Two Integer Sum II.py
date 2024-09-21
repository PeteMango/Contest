from bisect import bisect_left, bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            need = target - num

            # need 2 of the same numbers
            if need == num and bisect(numbers, need) - bisect_left(numbers, need) > 1:
                return [i+1, bisect(numbers, need)]
            # need two different numbers
            elif bisect_left(numbers, need) != bisect(numbers, need):
                return [i+1, bisect(numbers, need)]
            
        return [-1, -1]