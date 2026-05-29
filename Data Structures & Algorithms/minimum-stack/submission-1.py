class MinStack:

    def __init__(self):
        self.stack = []
        self.minny = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minny or self.minny[-1] >= val:
            self.minny.append(val)


    def pop(self) -> None:
        if self.stack.pop() == self.minny[-1]:
            self.minny.pop()

    def top(self) -> int:
        return self.stack[-1]

    # min element of stack in o(1) time
    def getMin(self) -> int:
        return self.minny[-1]
