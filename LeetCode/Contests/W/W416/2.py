class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        l, r = 0, 1 << 70
        workerTimes.sort()

        def canDo(T: int):
            total_height = 0
            for t_i in workerTimes:
                discriminant = 1 + (8 * T) // t_i
                if discriminant < 1:
                    x_i = 0
                else:
                    sqrt_discriminant = int(math.isqrt(discriminant))
                    x_i = (sqrt_discriminant - 1) // 2
                total_height += x_i
                if total_height >= mountainHeight:
                    return True
            return total_height >= mountainHeight
        
        while l <= r:
            mid = (l+r) // 2
            if canDo(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l

s = Solution()

mountainHeight = 4
workerTimes = [2,1,1]

mountainHeight = 10
workerTimes = [3,2,2,4]

mountainHeight = 5
workerTimes = [1]

print(s.minNumberOfSeconds(mountainHeight, workerTimes))
