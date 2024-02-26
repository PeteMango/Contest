from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_dict = []

        for auto in range(len(strs)):
            list_dict.append(defaultdict(int))

        for index, str in enumerate(strs):
            for c in str:
                list_dict[index][c] += 1

        ret = []

        for i in range(len(strs)):
            if strs[i] == "xd_tmp_string":
                continue

            t = []
            t.append(strs[i])
            strs[i] = "xd_tmp_string"

            for j in range(i+1, len(strs), 1):
                if list_dict[i].items() == list_dict[j].items() and strs[j] != "xd_tmp_string":
                    t.append(strs[j])
                    strs[j] = "xd_tmp_string"
            ret.append(t)

        return ret

s = Solution()

# strs = ["eat","tea","tan","ate","nat","bat"]

# strs = [""]

strs = ["a"]

print(s.groupAnagrams(strs))
