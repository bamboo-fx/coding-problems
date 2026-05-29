class MyQueue:
    """
    here we are using stacks which follow LIFO right and rearranging
    such that the order of elements being added in are still LIFO for stack
    but they are now original order FIFO for a queue
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        for pushing onto a queue, FIFO, but stack is LIFO, so to
        get latest pushed to be last out, we need to make it such that
        in our stack, the last on added, is the front of the stack
        """

        """
        i guess the logic has to be that, we want to move s1 to s2, then move it back
        in between is when we add to s1, because that means when we go s2 -> s1, the new
        thing is now first, and last in stack to get moved, thus first removed is first
        thing added
        """
        # self.s1 is our main, self.s2 is the temp
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        After pushing, self.s1 now contains the correct ordering of a queue
        so should just be stack[-1]
        """
        
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        if not self.s1:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()