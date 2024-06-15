# Thu, June 13, 2024

from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        ans = 0
        for seat, student in zip(seats, students):
            ans += abs(seat - student)
        return ans

s = Solution()

seats = [3,1,5]
students = [2,7,4]

seats = [4,1,5,9]
students = [1,3,2,6]

seats = [2,2,6,6]
students = [1,3,2,6]

print(s.minMovesToSeat(seats, students))
