from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        dict = defaultdict(list)

        for access in access_times:
            employee, time = access[0], access[1]

            dict[employee].append(time)

        ret = []

        for employee, access in dict.items():
            print(employee + ': ' + ', '.join(access))
            if self.isHighAccess(access):
                ret.append(employee)

        return ret

    def isHighAccess(self, access: List[str]) -> bool:
        if len(access) < 3:
            return False

        for i in range(len(access) - 2):
            for j in range(i+1, len(access)-1, 1):
                for k in range(j+1, len(access), 1):
                    if self.isSameHour(access[i], access[j]) and self.isSameHour(access[i], access[k]) and self.isSameHour(access[k], access[j]):
                        return True

        return False

    def isSameHour(self, time_a, time_b: str) -> bool:
        time_a_hour, time_a_min = time_a[:-2], time_a[2:]
        time_b_hour, time_b_min = time_b[:-2], time_b[2:]

        if time_a_hour == time_b_hour:
            return True

        if abs(int(time_a_hour) - int(time_b_hour)) > 1:
            return False

        if int(time_a_hour) > int(time_b_hour):
            return int(time_a_min) < int(time_b_min)
        elif int(time_b_hour) > int(time_a_hour):
            return int(time_a_min) > int(time_b_min)

        return False

s = Solution()
# access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
# access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]

# print(s.isSameHour("0549", "0532"))
# print(s.isSameHour("0549", "0621"))

print(s.findHighAccessEmployees(access_times))
