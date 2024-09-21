class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = defaultdict(int), defaultdict(int)
        for c in s:
            a[c] += 1
        for c in t:
            b[c] += 1
        
        if len(s) != len(t):
            return False
        
        for k in a:
            if a[k] != b[k]:
                return False
        return True