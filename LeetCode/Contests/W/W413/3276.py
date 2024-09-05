class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        # maps to value to rows that they appear in 
        d = defaultdict(set)
        for i in range(n):
            for j in range(m):
                d[grid[i][j]].add(i)

        @lru_cache(None)
        def dfs(val, mask): 
            # vis set based on row is not fast enough ???
            if val > 100: 
                return 0
            
            mx_val = dfs(val+1, mask)
            # print(f'val: {val}, mx_val: {mx_val}')
            for row in d[val]:
                if (mask & 1 << row):
                    continue
                mx_val = max(mx_val, val + dfs(val + 1, mask | (1 << row)))
        
            return mx_val

        return dfs(0, 0)
    
s = Solution()

grid = [[1,2,3],[4,3,2],[1,1,1]]

grid = [[8,7,6],[8,3,2]]

print(s.maxScore(grid))