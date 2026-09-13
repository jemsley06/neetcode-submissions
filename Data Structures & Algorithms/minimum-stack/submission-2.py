class MinStack:

    def __init__(self):
        self.items = []
        self.minval = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.minval:
            self.minval.append(val)
        elif val <= self.minval[len(self.minval) - 1]:
            self.minval.append(val)

    def pop(self) -> None:
        item = self.items.pop()
        if item == self.minval[len(self.minval) - 1]:
            self.minval.pop()
        return item

    def top(self) -> int:
        return self.items[len(self.items) - 1]

    def getMin(self) -> int:
        if self.minval:
            return self.minval[len(self.minval) - 1]
        else:
            return None
