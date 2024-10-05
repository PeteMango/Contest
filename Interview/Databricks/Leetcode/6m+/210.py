class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(set)
        if not prerequisites:
            return [i for i in range(n)]

        for a, b in prerequisites:
            d[a].add(b)

        vis = set()
        def findSync() -> List[int]:
            ret = []
            for i in range(n):
                if i in vis:
                    continue
                if i not in d or len(d[i]) == 0:
                    ret.append(i)
            
            return ret

        ans = []
        while len(vis) != n:
            sync = findSync()
            if not sync:
                break

            ans = ans + sync
            for s in sync:
                vis.add(s)
                for k, v in d.items():
                    if s in v:
                        v.remove(s)
        
        if len(ans) < n:
            return []

        return ans
