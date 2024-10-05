from bisect import bisect, bisect_left, insort
class SummaryRanges:

    def __init__(self):
        self.hasComputed = False
        self.ranges = []
        

    def addNum(self, value: int) -> None:
        if bisect_left(self.ranges, value, key=lambda a: a[1]) != bisect(self.ranges, value, key=lambda a: a[0]):
            return

        insort(self.ranges, (value, value), key=lambda a: a[0])
        self.hasComputed = False

    def getIntervals(self) -> List[List[int]]:
        print(f'here: {self.ranges}')
        if self.hasComputed:
            return self.ranges   

        new_interval = []
        start = 0
        while start < len(self.ranges):
            s, e = self.ranges[start]
            back = start + 1
            while back < len(self.ranges) and self.ranges[back][0] == e + 1:
                e = self.ranges[back][1]
                back += 1
            
            new_interval.append((s, e))
            start = back
        
        self.ranges = new_interval
        self.hasComputed = True
        return self.ranges


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()