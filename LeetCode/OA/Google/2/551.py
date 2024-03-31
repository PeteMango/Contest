class Solution:
    def checkRecord(self, s: str) -> bool:
        return self.lateThreeConsecutive(s) and self.absentTwoDays(s)

    def lateThreeConsecutive(self, s: str) -> bool:
        cnt = 1 if s[0] == 'L' else 0
        for i in range(1, len(s)):
            if cnt >= 3:
                return False
            if s[i] == 'L':
                cnt += 1
            else:
                cnt = 0

        return cnt < 3

    def absentTwoDays(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c == 'A':
                cnt += 1
        return cnt < 2

s = Solution()

str = "PPALLP"

str = "PPALLL"

print(s.checkRecord(str))
