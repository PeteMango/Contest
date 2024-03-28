from typing import List

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()

        mx_days = -1
        for job, worker in zip(jobs, workers):
            mx_days = max(mx_days, job // worker if job % worker == 0 else (job // worker) + 1)

        return mx_days

s = Solution()

jobs = [5,2,4]
workers = [1,7,5]

jobs = [3,18,15,9]
workers = [6,5,1,3]

print(s.minimumTime(jobs, workers))
