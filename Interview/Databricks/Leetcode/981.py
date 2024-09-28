class TimeMap:

    def __init__(self):
        self.d = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.d[key]:
            self.d[key] = [(timestamp, value)]
        else:
            bisect.insort(self.d[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.d[key], timestamp, key=lambda x: x[0])

        if idx > 0:
            return self.d[key][idx - 1][1]
         
        return ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)