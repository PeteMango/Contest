from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret, cur, num_letters = [],  [], 0
        for w in words:
            if num_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                ret.append(''.join(cur))

                # reset new line
                cur, num_letters= [], 0
            cur += [w]
            num_letters += len(w)
        return ret + [' '.join(cur).ljust(maxWidth)]

s = Solution()

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

ret = s.fullJustify(words, maxWidth)

for line in ret:
    print(line)
