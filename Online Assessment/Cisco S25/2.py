
"""
inputArr, represents the given array of element of size inputArr_size.
"""
def funcTwins(inputArr):
	st = set()
	for num in inputArr:
		if num in st:
			st.remove(num)
		else:
			st.add(num)

	if not st:
		return -1
	
	return min(st)

def main():
	#input for inputArr
	inputArr = []
	inputArr_size  = int(input())
	inputArr = list(map(int,input().split()))
	
	
	result = funcTwins(inputArr)
	print(result)	

if __name__ == "__main__":
	main()