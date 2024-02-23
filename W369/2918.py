from typing import List

class Solution:
    def minSum(self, a: List[int], b: List[int]) -> int:
        suma, zeroa, sumb, zerob = 0, 0, 0, 0

        for x in a:
            if x == 0:
                zeroa += 1
            suma += x

        for x in b:
            if x == 0:
                zerob += 1
            sumb += x

        if zeroa == 0 and ((sumb > suma) or (sumb == suma and zerob > 0) or (sumb + zerob > suma)):
            return -1

        if zerob == 0 and ((suma > sumb) or (sumb == suma and zeroa > 0) or (suma + zeroa > sumb)):
            return -1


        return max(suma + zeroa, sumb + zerob)

s = Solution()

nums1 = [2,0,2,0]
nums2 = [1,4]

# nums1 = [3,2,0,1,0]
# nums2 = [6,5,0]

print(s.minSum(nums1, nums2))
