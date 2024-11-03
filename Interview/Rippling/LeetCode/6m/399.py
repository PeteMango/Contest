class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        for i, [a, b], in enumerate(equations):
            d[a].append((b, values[i]))
            d[b].append((a, 1/values[i]))

        def solve(start: int, end: int):
            if start == end and start in d:
                return 1
            
            if start == end and start not in d:
                return -1
            
            if start not in d or end not in d:
                return -1
            
            vis = defaultdict(int)
            vis[start] = 1
            dq = deque()
            dq.append(start)
            while dq:
                f = dq.popleft()

                for n, v in d[f]:
                    if n not in vis:
                        dq.append(n)
                        vis[n] = vis[f] * v

            # print(f'for {start} {end} we get {vis}')

            if end not in vis:
                return -1

            return vis[end] 

        ans = []
        for s, e in queries:
            ans.append(solve(s, e))
        
        return ans