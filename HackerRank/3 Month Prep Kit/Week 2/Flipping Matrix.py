#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
from typing import List
def flippingMatrix(matrix: List[List[int]]) -> int:
    n = len(matrix) // 2
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += max(
            matrix[i][j], matrix[i][2*n-j-1],
            matrix[2*n-i-1][j], matrix[2*n-i-1][2*n-j-1]
            )
    return ans
