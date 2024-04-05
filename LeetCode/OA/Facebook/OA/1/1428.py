from typing import Optional, List

# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# class BinaryMatrix(object):
#     def get(self, row: int, col: int) -> int:
#         return 0
#     def dimensions(self) -> List[int]:
#         return []

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1]
        min_idx = m+1
        for i in range(n):
            val = self.binarySearch(binaryMatrix, i, m)
            if val != -1:
                min_idx = min(val, min_idx)

        return -1 if min_idx == m+1 else min_idx

    def binarySearch(self, binaryMatrix: 'BinaryMatrix', row, m: int) -> int:
        if binaryMatrix.get(row, m-1) == 0:
            return -1

        l, r = 0, m-1
        while l <= r:
            mid = (l + r) // 2
            if binaryMatrix.get(row, mid) == 1:
                r = mid - 1
            else:
                l = mid + 1

        return l
