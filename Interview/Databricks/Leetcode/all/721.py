class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = defaultdict(set)
        for account in accounts:
            name, email, n = account[0], account[1:], len(account) - 1
            for i in range(n):
                g[email[i]].add((email[i], name))
                for j in range(i+1, n):
                    g[email[i]].add((email[j],name))
                    g[email[j]].add((email[i], name))

        for k, v in g.items():
            print(f'{k} <-> {v}')

        seen = set()
        ret = []
        for k, v in g.items():
            if k in seen:
                continue
            
            q = deque()
            q.append(k)
            e = next(iter(v))
            t = []
            while q:
                f = q.popleft()
                t.append(f)
                seen.add(f)
                for neighbor in g[f]:
                    if neighbor[0] not in seen:
                        q.append(neighbor[0])
            
            t = list(set(t))
            t.sort()

            ret.append([e[1]]+t)

        return ret