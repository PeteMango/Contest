import random
class RandomizedSet:
    def __init__(self):
        self.unordered_set = set()

    def insert(self, val: int) -> bool:
        if val in self.unordered_set:
            return False

        self.unordered_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.unordered_set:
            self.unordered_set.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.unordered_set))


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_2 = obj.remove(0)
param_3 = obj.getRandom()

print(param_3)
