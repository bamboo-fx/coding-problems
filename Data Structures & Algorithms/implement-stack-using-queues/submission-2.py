class MyStack:

    def __init__(self):
        # create 2 queues
        self.q = deque()

    def push(self, x: int) -> None:
        # basically add to end right, now get that to front
        # to do so iterate till end - 1
        # starting from starting index, add that to end
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self) -> int:
        # remove from right for stack, left in queue
        return self.q.popleft()

    def top(self) -> int:
        # return front of queue
        return self.q[0]

    def empty(self) -> bool:
        if not self.q:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()