class TicTacToe:
    """
    n rows + n columns
    """
    def __init__(self, n: int):
        self.onex = defaultdict(int)
        self.oney = defaultdict(int)
        self.twox = defaultdict(int)
        self.twoy = defaultdict(int)
        self.g = [[0 for _ in range(n)] for _ in range(n)]

    def check_diagonal(self):
        n = len(self.g)
        found = True
        for i in range(1, n):
            if self.g[i][i] != self.g[i-1][i-1] or self.g[i][i] == 0:
                found = False
                break
        
        if found:
            return 1 if self.g[0][0] == 'X' else 2
        
        found = True
        for i in range(1, n):
            if self.g[i][n-i-1] != self.g[i-1][n-i] or self.g[i][n-i-1] == 0:
                found = False
                break
        
        if found:
            return 1 if self.g[n-1][0] == 'X' else 2
        
        return -1

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.g)
        if player == 1:
            self.onex[row] += 1
            self.oney[col] += 1
        else:
            self.twox[row] += 1
            self.twoy[col] += 1
        
        self.g[row][col] = 'X' if player == 1 else 'O'

        # print('grid:')
        # for r in self.g:
        #     print(r)


        if self.check_diagonal() != -1:
            return self.check_diagonal()
        

        for k, v in self.onex.items():
            if v == n:
                return 1
        for k, v in self.oney.items():
            if v == n:
                return 1
        
        for k, v in self.twox.items():
            if v == n:
                return 2
        for k, v in self.twoy.items():
            if v == n:
                return 2
        
        return 0




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)