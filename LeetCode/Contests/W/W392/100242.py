class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        to_int = []
        for c in s:
            to_int.append(max(0, ord(c)-97))

        print(to_int)

        idx = 0
        while k >= 0 and idx < len(s):
            cur = to_int[idx]

            if cur == 0:
                idx += 1
                continue

            l, r = to_int[idx], 26 - to_int[idx]

            if l < r and k >= l:
                k -= l
                to_int[idx] = 0
            elif r <= l and k >= r:
                k -= r
                to_int[idx] = 0
            else:
                to_int[idx] -= k
                k = 0

            idx += 1

        print(to_int)
        ret = ''
        for num in to_int:
            ret += chr(num+97)

        return ret

s = Solution()

str = "zbbz"
k = 3

str = "xaxcd"
k = 4

str = "lol"
k = 0

print(s.getSmallestString(str, k))
