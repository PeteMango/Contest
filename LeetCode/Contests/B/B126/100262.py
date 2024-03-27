from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            nums[idx] = self.replace(num, self.findmx(num))

        sum = 0

        for num in nums:
            sum += num

        return sum


    def findmx(self, x: int) -> int:
        dig = []
        while x > 0:
            dig.append(x % 10)
            x = int(x/10)

        dig.sort()
        return dig[-1]

    def replace(self, x, rep: int) -> int:
        length = len(str(x))

        ret = ""
        for i in range(length):
            ret += str(rep)

        return int(ret)

s = Solution()

nums = [1,2,3]

nums = [10,21,31]

print(s.sumOfEncryptedInt(nums))
