# Sparse Table for Range Min/Max Query Implementation

from typing import List
from math import log2

class SparseTable:
    def __init__(self, nums: List[int]):
        """
        Initialize sparse table from a list of integers

        Args:
            nums (list[int]): list of integers to compute sparse table for
        """

        self.n = len(nums)
        if self.n == 0:
            raise ValueError("Input list is empty")

        self.max_log = int(log2(self.n)) + 1
        self.min_sparse = [[0] * self.max_log for _ in range(self.n)]
        self.max_sparse = [[0] * self.max_log for _ in range(self.n)]

        for i in range(self.n):
            self.min_sparse[i][0] = nums[i]
            self.max_sparse[i][0] = nums[i]

        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.min_sparse[i][j] = min(self.min_sparse[i][j - 1], self.min_sparse[i + (1 << (j - 1))][j - 1])
                self.max_sparse[i][j] = max(self.max_sparse[i][j - 1], self.max_sparse[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query_max(self, l: int, r: int) -> int:
        """
        Compute range max for range [l, r]

        Args:
            l (int): left index of query
            r (int): right index of query

        Returns:
            max (int): maxmium number in range
        """

        j = int(log2(r - l + 1))
        return max(self.max_sparse[l][j], self.max_sparse[r - (1 << j) + 1][j])

    def query_min(self, l: int, r: int) -> int:
        """
        Compute range min for range [l, r]

        Args:
            l (int): left index of query
            r (int): right index of query

        Returns:
            min (int): min number in range
        """

        j = int(log2(r - l + 1))
        return min(self.min_sparse[l][j], self.min_sparse[r - (1 << j) + 1][j])
