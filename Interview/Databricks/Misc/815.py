class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n, canStart, canEnd, d = len(routes), set(), set(), defaultdict(set)
        if source == target:
            return 0
            
        for i in range(n):
            routes[i] = tuple(routes[i])
        ht = defaultdict(tuple)
        for r in routes:
            ht[hash(r)] = r

        for i in range(n):
            if source in routes[i]:
                canStart.add(hash(routes[i]))
            if target in routes[i]:
                canEnd.add(hash(routes[i]))
            for j in range(i+1, n):
                if set(routes[i]).intersection(set(routes[j])):
                    d[hash(routes[i])].add(hash(routes[j]))
                    d[hash(routes[j])].add(hash(routes[i]))

        min_bus = 10**5 + 5
        for start in canStart:
            q = deque([start])
            dist = defaultdict(int)
            dist[start] = 1
            while q:
                f = q.popleft()
                for neighbor in d[f]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[f] + 1
                        q.append(neighbor)
                    elif dist[neighbor] > dist[f] + 1:
                        dist[neighbor] = dist[f] + 1
                        q.append(neighbor)
            
            for e in canEnd:
                if e in dist:
                    min_bus = min(min_bus, dist[e])

        return -1 if min_bus == 10**5 + 5 else min_bus