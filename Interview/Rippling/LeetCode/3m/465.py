class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = [0] * 13
        for f, t, a in transactions:
            debt[f] -= a
            debt[t] += a
        
        def dfs(cur_idx: int):
            if cur_idx == 12:
                return 0
            
            if debt[cur_idx] == 0:
                return dfs(cur_idx + 1)
            
            min_transactions, final_to = 10**5 + 5, -1

            for j in range(cur_idx + 1, 13):
                if debt[cur_idx] * debt[j] < 0:
                    debt[j] += debt[cur_idx]

                    min_transactions = min(min_transactions, 1 + dfs(cur_idx + 1))

                    debt[j] -= debt[cur_idx]

            return min_transactions
        
        return dfs(0)