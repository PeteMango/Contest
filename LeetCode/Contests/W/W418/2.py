class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        d = defaultdict(set)
        for x, y in invocations:
            d[x].add(y)
        
        q = deque()
        q.append(k)
        vis = set()
        while q:
            f = q.popleft()
            vis.add(f)
            for inv in d[f]:
                if inv in vis:
                    continue
                q.append(inv)
        
        numbers = [i for i in range(n)]
        not_vis = set(numbers).difference(vis)
        for nv in not_vis:
            if d[nv].intersection(vis):
                return numbers
        return list(not_vis)
