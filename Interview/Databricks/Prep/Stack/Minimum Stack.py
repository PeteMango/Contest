class MinStack:

    def __init__(self):
        self.sk = []

    def push(self, val: int) -> None:
        if not self.sk:
            self.sk.append((val, val))
            return
        self.sk.append((val, min(val, self.sk[-1][1])))

    def pop(self) -> None:
        self.sk.pop()

    def top(self) -> int:
        return self.sk[-1][0]

    def getMin(self) -> int:
        return self.sk[-1][1]
