from typing import List

class Solution:
    def maxManhattanDistance(self, points: List[List[int]]) -> (int, List[int], List[int]):
        plus = [x + y for x, y in points]
        minus = [x - y for x, y in points]
        max_plus, min_plus = max(plus), min(plus)
        max_minus, min_minus = max(minus), min(minus)

        max_plus_indices = [i for i, val in enumerate(plus) if val == max_plus]
        min_plus_indices = [i for i, val in enumerate(plus) if val == min_plus]
        max_minus_indices = [i for i, val in enumerate(minus) if val == max_minus]
        min_minus_indices = [i for i, val in enumerate(minus) if val == min_minus]

        return (max(max_plus - min_plus, max_minus - min_minus),
                max_plus_indices + min_plus_indices,
                max_minus_indices + min_minus_indices)

    def minimumDistance(self, points: List[List[int]]) -> int:
        original_distance, plus_contributors, minus_contributors = self.maxManhattanDistance(points)
        min_distance_after_removal = original_distance

        critical_indices = set(plus_contributors + minus_contributors)

        for i in critical_indices:
            new_points = [p for j, p in enumerate(points) if j != i]
            new_max_distance, _, _ = self.maxManhattanDistance(new_points)
            min_distance_after_removal = min(min_distance_after_removal, new_max_distance)

        return min_distance_after_removal

s = Solution()

points = [[3,10],[5,15],[10,2],[4,4]]

points = [[1,1],[1,1],[1,1]]

points = [[7,9],[1,10],[6,10],[7,3],[9,2],[9,10],[7,10],[10,4],[4,10],[5,4]]

print(s.minimumDistance(points))
