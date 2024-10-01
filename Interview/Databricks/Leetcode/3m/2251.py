class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        e = Counter()
        ep = set(people)
        for x, y in flowers:
            e[x] += 1 
            e[y+1] -= 1
            ep.add(x)
            ep.add(y+1)
        
        flowers = defaultdict(int)
        bloom = 0

        for p in sorted(ep):
            bloom += e[p]
            flowers[p] = bloom
        
        return [flowers[p] for p in people]