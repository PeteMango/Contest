class Solution:
    def validSubstringCount(self, a: str, b: str) -> int:
        need = defaultdict(int)
        for c in b:
            need[c] += 1

        n, req = len(a), len(b)
        have = defaultdict(int)
        cur, start, ret = 0, 0, 0

        for ep in range(n):
            c = a[ep]
            have[c] += 1

            if have[c] <= need[c]:
                cur += 1

            while cur == req:
                ret += n - ep
                have[a[start]] -= 1

                if have[a[start]] < need[a[start]]:
                    cur -= 1

                start += 1

        return ret
    
s = Solution()

word1 = "bcca"
word2 = "abc"

word1 = "abcabc"
word2 = "abc"

word1 = "abcabc"
word2 = "aaabc"

print(s.validSubstringCount(word1, word2))