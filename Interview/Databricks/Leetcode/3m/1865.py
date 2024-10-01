class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.a = nums1
        self.b = nums2
        self.d = defaultdict(int)
        for num in nums2:
            self.d[num] += 1

    def add(self, index: int, val: int) -> None:
        v = self.b[index]
        self.b[index] += val
        self.d[v] -= 1
        self.d[self.b[index]] += 1

    def count(self, tot: int) -> int:
        ret = 0
        for num in self.a:
            if tot-num not in self.d:
                continue
            ret += self.d[tot - num]
        
        return ret


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)