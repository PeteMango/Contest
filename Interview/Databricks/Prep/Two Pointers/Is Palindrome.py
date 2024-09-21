class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed = ''
        for c in s:
            if c.isalpha() or c.isnumeric():
                removed += c.lower()
        
        l, r = 0, len(removed) - 1
        while l <= r:
            if removed[l] != removed[r]:
                return False
            l += 1
            r -= 1
        
        return True