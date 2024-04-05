from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        delta = abs((d2 - d1).days)

        return delta

s = Solution()

date1 = "2019-06-29"
date2 = "2019-06-30"

date1 = "2020-01-15"
date2 = "2019-12-31"

print(s.daysBetweenDates(date1, date2))
