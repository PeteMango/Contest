from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        letter = []

        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda log: log.split()[0])
        letter.sort(key=lambda log: log.split()[1:])

        return letter + dig

s = Solution()

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

print(s.reorderLogFiles(logs))
