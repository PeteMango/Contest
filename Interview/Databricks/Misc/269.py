class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n, d, seen = len(words), defaultdict(set), set()
        for w in words:
            for c in w:
                seen.add(c)

        for i in range(n):
            for j in range(i+1, n):
                sz = min(len(words[i]), len(words[j]))
                idx = 0
                while idx < sz:
                    if words[i][idx] == words[j][idx]:
                        idx += 1
                        continue
                    
                    d[words[i][idx]].add(words[j][idx])
                    break

                if idx == sz and len(words[i]) > len(words[j]):
                    return ""
            
        vis = set()
        def findSink() -> List[str]:
            ret = []
            for c in seen:
                if c in vis:
                    continue
                
                if c not in d or len(d[c]) == 0:
                    ret.append(c)
            
            return ret
        
        ans = []
        while len(vis) != len(seen):
            sink = findSink()
            # print(f'sink {sink}')
            if not sink:
                break
            
            ans = sink + ans
            for s in sink:
                vis.add(s)
                for k, v in d.items():
                    if s in v:
                        d[k].remove(s)
        
        if len(ans) == len(seen):
            return "".join(ans)
        
        return ""

            
                    
