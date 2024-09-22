class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        cnt = 2
        for w in message:
            if w in banned:
                cnt -=1
        
        return cnt <= 0

s = Solution()

message = ["hello","world","leetcode"]
bannedWords = ["world","hello"]

message = ["hello","programming","fun"]
bannedWords = ["world","programming","leetcode"]

print(s.reportSpam(message, bannedWords))