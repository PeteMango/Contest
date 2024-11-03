class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def checkExist(k: int) -> bool:
            vis = set()
            for i in range(len(s) - k + 1):
                h = hash(s[i:i+k])
                if h in vis:
                    return s[i:i+k]
                
                vis.add(h)

            return ""
        
        l, r = 0, len(s)
        mx_substring = ""
        while l <= r:
            mid = (l+r)//2
            check = checkExist(mid)

            # print(f'{mid} {check}')

            if check != "":
                mx_substring = check
                l = mid + 1
            else:
                r = mid - 1
        
        return mx_substring
