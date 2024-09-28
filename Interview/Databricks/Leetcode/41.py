class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        found = [0] * int(1e5 + 5)

        for x in nums:
            if x >= 0 and x < 1e5 + 5:
                found[x] += 1

        for i in range(1, len(found)):
            if found[i] == 0:
                return i
    
        return -1