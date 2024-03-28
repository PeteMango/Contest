from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))

        print(intervals)

        ret = []
        start = 0
        mx_right = intervals[0][1]

        for i in range(1, len(intervals)):
            print(f'{mx_right}')
            if intervals[i][0] <= mx_right:
                mx_right = max(mx_right, intervals[i][1])
                continue
            else:
                ret.append([intervals[start][0], mx_right])
                start = i
                mx_right = intervals[i][1]


        ret.append([intervals[start][0], mx_right])

        return ret

s = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]

# intervals = [[1,4],[4,5]]

# intervals = [[1,4],[2,3]]

# intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

print(s.merge(intervals))
