from bisect import bisect, bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, l, r = -1, 0, len(matrix)-1

        while l <= r:
            row = (l + r) // 2
            if matrix[row][0] <= target and matrix[row][-1] >= target:
                break
            elif matrix[row][0] > target:
                r = row - 1
            else:
                l = row + 1
        
        return bisect_left(matrix[row], target) != bisect(matrix[row], target)