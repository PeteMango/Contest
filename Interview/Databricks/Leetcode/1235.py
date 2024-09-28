from bisect import bisect, bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for s, e, p in zip(startTime, endTime, profit):
            jobs.append((e, s, p))

        n = len(jobs)
        jobs.sort()
        print(jobs)

        # 0 -> take, 1 -> don't take
        dp = [0 for _ in range(n)]
        dp[0] = jobs[0][2]
        
        for i in range(1, n):
            e, s, p = jobs[i]
            idx = bisect(jobs, s, key = lambda i: i[0])
            if idx == 0:
                dp[i] = max(dp[i-1], p)
            else:
                dp[i] = max(dp[i-1], dp[idx-1] + p)

        return dp[-1]