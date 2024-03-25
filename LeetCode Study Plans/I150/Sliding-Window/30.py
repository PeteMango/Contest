from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        str_len = len(words[0])

        dict = defaultdict(int)

        for word in words:
            dict[word] += 1

        substr_len = str_len * len(words)

        ret = []

        for i in range(0, len(s) - substr_len + 1):
            seen_words = defaultdict(int)

            for j in range(0, substr_len, str_len):
                word = s[i + j:i + j + str_len]

                if word in dict:
                    seen_words[word] += 1

                    if seen_words[word] > dict[word]:
                        break
                else:
                    break

            if seen_words == dict:
                ret.append(i)

        return ret



s = Solution()

# str = "barfoothefoobarman"
# words = ["foo","bar"]

# str = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]

str = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

print(s.findSubstring(str, words))
