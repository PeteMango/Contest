class Leaderboard:

    def __init__(self):
        self.d = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.d[playerId] += score

    def top(self, K: int) -> int:
        scores = []
        for k, v in self.d.items():
            if len(scores) >= K:
                if scores[0] < v:
                    heappop(scores)
                    heappush(scores, v)
            else:
                heappush(scores, v)
            
        return sum(scores)

    def reset(self, playerId: int) -> None:
        self.d[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)