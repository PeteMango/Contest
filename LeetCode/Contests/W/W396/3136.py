class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        for c in word:
            if not c.isalpha() and not c.isnumeric():
                return False

        if not set('aeiou').intersection(word.lower()):
            return False
        if not set('bcdfghjklmnpqrstvwxyz').intersection(word.lower()):
            return False

        return True

s = Solution()

word = "234Adas"

word = "b3"

word = "a3$e"

print(s.isValid(word))
