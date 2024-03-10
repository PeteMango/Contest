from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ret = []

        for s in arr:
            ret.append(self.smallest_uncommon_substr(s, arr))

        return ret

    def smallest_uncommon_substr(self, s: str, arr: List[str]) -> str:
        n = len(s)

        pos = []

        for substr_len in range(1, n+1):
            for i in range(0, n - substr_len + 1):
                substr = s[i:i+substr_len]

                if not self.in_other_elements(s, substr, arr):
                    pos.append(substr)

        if len(pos) == 0:
            return ""

        return min(pos, key=lambda x: (len(x), x))

    def in_other_elements(self, s, substr: str, arr: List[str]) -> bool:
        for string in arr:
            if string == s:
                continue
            if substr in string:
                return True

        cnt = 0
        for string in arr:
            if string == substr:
                cnt += 1

        if cnt > 1:
            return True
        return False

s = Solution()

# arr = ["cab","ad","bad","c"]

# arr = ["abc","bcd","abcd"]

arr = ["fhi","ct","s","o","o"]

print(s.shortestSubstrings(arr))
