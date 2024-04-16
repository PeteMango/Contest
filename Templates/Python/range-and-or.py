from typing import List
import numpy as np

class RangeAndQueries:
    def __init__(self, arr: List[int]):
        self.MAX = 100000
        self.bitscount = 32
        self.prefix_count = np.zeros((self.bitscount, self.MAX))
        self.find_prefix_count(arr)

    def find_prefix_count(self, arr: List[int]) -> None:
        """
        Function to find the prefix count

        Args:
            arr (List[int]): Input array
        """
        n = len(arr)
        for i in range(self.bitscount):
            self.prefix_count[i][0] = ((arr[0] >> i) & 1)
            for j in range(1, n):
                self.prefix_count[i][j] = ((arr[j] >> i) & 1)
                self.prefix_count[i][j] += self.prefix_count[i][j - 1]

    def range_and(self, l: int, r: int) -> int:
        """
        Function to answer range AND query

        Args:
            l (int): Left index of the range
            r (int): Right index of the range

        Returns:
            int: Result of range AND query
        """
        ans = 2**31 - 1  # Initialize answer with all bits set to 1
        for i in range(self.bitscount):
            x = 0
            if l == 0:
                x = self.prefix_count[i][r]
            else:
                x = self.prefix_count[i][r] - self.prefix_count[i][l - 1]
            if x == r - l + 1:
                ans &= ~(1 << i)
        return ans

    def multiple_range_and_queries(self, queries: List[List[int]]) -> List[int]:
        """
        Function to answer multiple range AND queries

        Args:
            queries (List[List[int]]): List of query ranges

        Returns:
            List[int]: List of results for each query
        """

        results = []
        for query in queries:
            results.append(self.range_and(query[0], query[1]))
        return results
