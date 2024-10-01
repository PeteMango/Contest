class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        ngrid = [['' for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                ngrid[i][j] = box[n - j - 1][i]

        for i in range(m-1, -1, -1):
            for j in range(n):
                if ngrid[i][j] == '.':
                    for k in range(i-1, -1, -1):
                        if ngrid[k][j] == '*':
                            break
                        elif ngrid[k][j] == '#':
                            ngrid[k][j] = '.'
                            ngrid[i][j] = '#'
                            break
    
        for row in ngrid:
            print(row)

        return ngrid
        