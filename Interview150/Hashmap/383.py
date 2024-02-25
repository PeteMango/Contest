from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = defaultdict(int)
        magazine_map = defaultdict(int)

        for c in ransomNote:
            ransom_map[c] += 1

        for c in magazine:
            magazine_map[c] += 1

        for key in ransom_map:
            if ransom_map[key] > magazine_map[key]:
                return False

        return True

s = Solution()

# ransomNote = "a"
# magazine = "b"

# ransomNote = "aa"
# magazine = "ab"

# ransomNote = "aa"
# magazine = "aab"

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

print(s.canConstruct(ransomNote, magazine))
