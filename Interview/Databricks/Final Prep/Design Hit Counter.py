from bisect import bisect
class HitCounter:
    def __init__(self):
        self.tl = []

    def hit(self, timestamp: int) -> None:
        self.tl.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.tl) - bisect(self.tl, timestamp-300)

# 1 2 3 300

hc = HitCounter()

hc.hit(1)
hc.hit(2)
hc.hit(3)

assert hc.getHits(4) == 3

hc.hit(300)
hc.getHits(300)

assert hc.getHits(300) == 4
assert hc.getHits(301) == 3
