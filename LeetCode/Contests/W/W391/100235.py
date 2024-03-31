class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            print(f'{numBottles} {numExchange}')
            ans += 1
            numBottles = numBottles - numExchange + 1
            numExchange += 1

        print(f'{numBottles} {numExchange}')

        return ans

s = Solution()

numBottles = 13
numExchange = 6

# numBottles = 10
# numExchange = 3

print(s.maxBottlesDrunk(numBottles, numExchange))
