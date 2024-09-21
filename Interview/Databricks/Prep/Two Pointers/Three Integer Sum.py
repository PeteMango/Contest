class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ret = set()

        for i, num in enumerate(nums):
            # break cause pos + pos never = 0
            if num > 0:
                break

            # remove duplicate
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            while l < r:
                if num + nums[l] + nums[r] == 0:
                    ret.add((num, nums[l], nums[r]))
                    l += 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        
        ans = []
        for t in ret:
            ans.append([t[0], t[1], t[2]])

        return ans