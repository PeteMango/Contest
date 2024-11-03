from bisect import bisect_left, bisect

class AnalyticalData:
    def __init__(self):
        self.psa = []
  
    def insert(self, transactionId: str, timestamp: int, amount: int) -> None:
        if len(self.psa) == 0:
            self.psa.append((timestamp, transactionId, amount))
            return
        
        self.psa.append((timestamp, transactionId, amount + self.psa[-1][2]))
    
    def rangeQuery(self, startTime: int, endTime: int) -> int:
        left_idx = bisect_left(self.psa, startTime, key=lambda a: a[0])
        right_idx = bisect(self.psa, endTime, key=lambda a: a[0])

        if left_idx == 0:
            return self.psa[right_idx]
        
        return self.psa[right_idx] - self.psa[left_idx]
    
ad = AnalyticalData()

ad.insert("a", 10, 10)
ad.insert("b", 20, 20)

print(ad.rangeQuery(0, 10))