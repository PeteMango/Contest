from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))

        n = int(1e6 + 5)
        d = [0] * n

        for interval in intervals:
            self.update(interval[0], interval[1]-1, 1, d)

        a = [0] * n
        a[0] = d[0]
        for i in range(1, len(d)):
            a[i] = a[i-1] + d[i]

        mx = 1
        for i in range(int(1e6 + 5)):
            mx = max(a[i], mx)

        return mx

    def update(self, l, r, val: int, d: List[int]) -> None:
        d[l] += val

        if r + 1 < len(d):
            d[r+1] -= val

s = Solution()

intervals = [[0,30],[5,10],[15,20]]

intervals = [[7,10],[2,4]]

intervals = [[13,15],[1,13]]

print(s.minMeetingRooms(intervals))
