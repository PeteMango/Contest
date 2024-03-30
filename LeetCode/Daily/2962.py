# Fri, March 29, 2024

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx_element, num_occurance = nums[0], 0

        for num in nums:
            mx_element = max(mx_element, num)

        for num in nums:
            if num == mx_element:
                num_occurance += 1

        return self.subarrayAtLeastK(nums, k, mx_element)

    def subarrayAtLeastK(self, nums: List[int], k, mx_element: int) -> int:
        l, r, cnt, ans = 0, 0, 0, 0
        while l <= r and r < len(nums):
            if nums[r] == mx_element:
                cnt +=1

            while cnt >= k:
                ans += len(nums) - r

                if nums[l] == mx_element:
                    cnt -= 1

                l += 1

            r += 1
        return ans

s = Solution()

nums = [1,3,2,3,3]
k = 2

# nums = [1,4,2,1]
# k = 3

print(s.countSubarrays(nums, k))
