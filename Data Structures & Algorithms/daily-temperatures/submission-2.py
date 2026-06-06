class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        so basically we are creating a results array where the value at index in results
        corresponds to the number of temperatures since that corresponding index
        in temperatures before a temperature greater shows up.
        
        We solve this problem using a stack, where the stack contains temperatures
        that are yet to have found a temperature greater than them, so we iterate
        through temperature, whenever we do find a temperature greater than top of stack
        what we do is we pop from stack, then add the index of current temp - index of top of stack
        we do this in a while loop since one temperature later on could be greater than a couple

        So essentially the stack is key, we use it to track all temperatures which are yet
        to have found a temperature greater, and LIFO works because, we always first compare most recent
        temp with current one then pop, then we can continue iterating through stack.
        If it was a queue instead then that wouldn't work because the first element might not necessarily
        be less than current temp, stack just really easy to track latest

        Other key is to track index for temperature too so use enumerate
        """
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                s_temp, s_index = stack.pop()
                result[s_index] = index - s_index
            stack.append((temp, index))
        return result