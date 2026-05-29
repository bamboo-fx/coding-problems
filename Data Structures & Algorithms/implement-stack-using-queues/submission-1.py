class MyStack:

    def __init__(self):
        # create 2 queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # add to second queue, while first queue is not empty
        # add the left most, left most is most recent
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        # swap q1 and q2 again, because q2 always empty and stores new head
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # for a stack: remove last in (right thing)
        # for a queue, removing the first thing
        return self.q1.popleft()

    def top(self) -> int:
        # for a stack: return last in (right thing)
        # for a queue: return left thing
        # just return left thing, keep list though
        return self.q1[0]
    def empty(self) -> bool:
        if not self.q1:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()