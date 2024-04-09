# Sun, April 7, 2024

from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque()
        s = deque()
        for student in students:
            q.append(student)

        for sandwich in sandwiches:
            s.append(sandwich)

        while q:
            stop = True

            for student in q:
                if student == s[0]:
                    stop = False
                    break

            if stop:
                break

            cur = q.popleft()
            if cur == s[0]:
                s.popleft()
            else:
                q.append(cur)

        return len(q)

s = Solution()

students = [1,1,0,0]
sandwiches = [0,1,0,1]

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

print(s.countStudents(students, sandwiches))
