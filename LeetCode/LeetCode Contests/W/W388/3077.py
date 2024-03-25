from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        psa = []

        for i, num in enumerate(nums):
            if i == 0:
                psa.append(nums[i])
            else:
                psa.append(psa[-1] + nums[i])

        # ? ? ? 9% ac ggwp
