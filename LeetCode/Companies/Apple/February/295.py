from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.append(num)

    def findMedian(self) -> float:
        if len(self.sl) % 2 == 0:
            l, r = self.sl[len(self.sl) // 2 - 1], self.sl[len(self.sl) // 2]

            return float((l + r) / 2)
        else:
            return self.sl[len(self.sl) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
