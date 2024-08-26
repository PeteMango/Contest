
"""
matrix, represents the elements of the matrix of size N*M.
"""
def funcMatrix(matrix):
	n, m = len(matrix), len(matrix[0])
	def found(x, y: int) -> bool:
		num = matrix[x][y]

		max_row, min_col = num, num

		for i in range(n):
			min_col = min(min_col, matrix[i][y])
		
		for j in range(m):
			max_row = max(max_row, matrix[x][j])
		
		return max_row == num and min_col == num

	for i in range(n):
		for j in range(m):
			if found(i, j):
				return matrix[i][j]

	return -1

def main():
	#input for matrix
	matrix = []
	matrix_rows,matrix_cols  = map(int, input().split())
	for idx in range(matrix_rows):
		matrix.append(list(map(int, input().split())))
	
	
	result = funcMatrix(matrix)
	print(result)	

if __name__ == "__main__":
	main()