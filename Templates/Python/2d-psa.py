# Prefix Sum Array 2-Dimensions Implementation

from typing import List

class PrefixSum2D:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            raise ValueError("Matrix is empty or undefined")

        self.rows, self.cols = len(matrix), len(matrix[0])
        self.psa = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                self.psa[r][c] = matrix[r-1][c-1] + self.psa[r-1][c] + self.psa[r][c-1] - self.psa[r-1][c-1]

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Compute sum of region from (row1, col1) to (row2, col2)

        Args:
            row1, col1 (int, int): Top-left corner of the sub-rectangle
            row2, col2 (int, int): Bottom-right corner of the sub-rectangle

        Returns:
            int: Sum of the sub-rectangle
        """
        return self.psa[row2+1][col2+1] - self.psa[row2+1][col1] - self.psa[row1][col2+1] + self.psa[row1][col1]
