from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        length, min_len = 0, 205

        for string in strs:
            min_len = min(min_len, len(string))


        ret = ""
        while length <= min_len:
            prefix = strs[0][0:length]

            if self.checkAll(strs, prefix):
                ret = strs[0][0:length]
                length += 1
            else:
                break

        return ret

    def checkAll(self, strs: List[str], prefix: str) -> bool:
        for s in strs:
            if s[0:len(prefix)] != prefix:
                return False

        return True

s = Solution()

strs = ["flower","flow","flight"]

strs = ["dog","racecar","car"]

strs = ["ab", "a"]

print(s.longestCommonPrefix(strs))
