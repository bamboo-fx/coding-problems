class StockSpanner:
    """
    Alright what they are asking us to do is implement the StockSpanner class
    The main thing is the next function, essentially call next with a price
    Then we check if price including itself, consecutive previous stock prices
    less than or equal to price and add that number to return object

    I think the key here is stack, we have a results array we can initialize to like 0 or something (I'll figure this out later)
    Then we have a stack, where we just use it to constantly peek at the most recent one
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        counter = 1
        temp = self.stack[:]
        while temp and temp[-1] <= price:
            counter += 1
            temp.pop()
        self.stack.append(price)
        return counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)