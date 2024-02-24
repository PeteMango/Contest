class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove = ""

        for c in s:
            if c == ' ':
                continue
            if self.isLetter(c) or self.isNumber(c):
                remove += c

        print(f'remove is: {remove}')

        n = len(remove)

        for i in range(0, int(n/2)):
            if (remove[i] == remove[n-i-1]) or \
                (abs(ord(remove[i]) - ord(remove[n - i - 1])) == 32 and \
                    (self.isLetter(remove[i]) and self.isLetter(remove[len(remove) - i - 1]))):
                continue
            else:
                return False
        return True

    def isLetter(self, c: str) -> bool:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            return True

        return False

    def isNumber(self, c: str) -> bool:
        if (ord(c) >= ord('0') and ord(c) <= ord('9')):
            return True

        return False


s = Solution()

# str = "A man, a plan, a canal: Panama"
str = "0P"
print(s.isPalindrome(str))
