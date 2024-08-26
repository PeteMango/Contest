
"""
grid, represents the letters in the grid of size N*M.
word, represents the words to be searched of size K.
"""
def funcPuzzle(grid, words):
	# Write your code here
	n, m = len(grid), len(grid[0])
	# print("n: ", n, "m: ", m)

	def find(x, y, word):
		length = len(word)
		if y + length <= m and ''.join(grid[x][y:y + length]) == word:
			return True
		if y - length + 1 >= 0 and ''.join(grid[x][y - length + 1:y + 1][::-1]) == word:
			return True
		if x + length <= n and ''.join([grid[i][y] for i in range(x, x + length)]) == word:
			return True
		if x - length + 1 >= 0 and ''.join([grid[i][y] for i in range(x - length + 1, x + 1)][::-1]) == word:
			return True
        
		return False

	ans = []
	for word in words:
		found = False
		for i in range(n):
			if found:
				break
			for j in range(m):
				if grid[i][j] == word[0] and find(i, j, word):
					ans.append("Yes")
					found = True
					break
		if not found:
			ans.append("No")

	return ' '.join(ans)

def main():
	#input for grid
	grid = []
	grid_rows,grid_cols  = map(int, input().split())
	for idx in range(grid_rows):
		grid.append(list(map(str, input().split())))
	
	#input for word
	word = []
	word_size  = int(input())
	word = list(map(str,input().split()))
	
	
	result = funcPuzzle(grid, word)
	print(result)	

if __name__ == "__main__":
	main()