class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start):
            if start == len(nums):
                permutations.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        permutations = []
        backtrack(0)
        return permutations

s = Solution()

nums = [1,2,3]

nums = [0,1]

nums = [1]

print(s.permute(nums))
