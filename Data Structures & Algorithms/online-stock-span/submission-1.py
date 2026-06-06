class StockSpanner:
    """
    Alright what they are asking us to do is implement the StockSpanner class
    The main thing is the next function, essentially call next with a price
    Then we check if price including itself, consecutive previous stock prices
    less than or equal to price and add that number to return object

    I think the key here is stack, we have a results array we can initialize to like 0 or something (I'll figure this out later)
    Then we have a stack, where we just use it to constantly peek at the most recent one
    
    I'm trying to write out a more efficient solution where I don't create
    a temporary copy of the stack, what I am thinking instead is pop from stack
    ok that's fine, but what about the idea that, if a current price in stack right,
    if it is less than or equal to the next price, then all values of that price on stack
    would also be less than or equal right, so instead we just add on to it
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        counter = 1
        while self.stack and self.stack[-1][0] <= price:
            counter += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, counter))
        return counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)