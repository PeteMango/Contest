from collections import defaultdict

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        d = defaultdict(list)
        for idx, c in enumerate(s):
            d[c].append(idx)

        alph = 'abcdefghijklmnopqrstuvwxyz'

        to_add = []
        for idx, c in enumerate(s):
            if c == '?':
                added = False
                for alphabet in alph:
                    if alphabet not in d:
                        to_add.append(alphabet)
                        d[alphabet].append(idx)
                        added = True
                        break
                if added:
                    continue

                min_cnt, min_char = 100000, ''
                for alphabet in alph:
                    if len(d[alphabet]) < min_cnt:
                        min_cnt = len(d[alphabet])
                        min_char = alphabet

                to_add.append(min_char)
                d[min_char].append(idx)


        to_add.sort()
        idx = 0
        ret = ""
        for c in s:
            if c == '?':
                ret += to_add[idx]
                idx += 1
            else:
                ret += c
        return ret

s = Solution()

str = "a?a?"

# str = "abcdefghijklmnopqrstuvwxy??"

# str = "???"

print(s.minimizeStringValue(str))
