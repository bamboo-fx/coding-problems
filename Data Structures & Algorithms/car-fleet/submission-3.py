class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Got it. So how it works is that we first get an array of tuples
        and first form tuples of the position and speed of the cars. Then
        we sort in decreaseing order in terms of positions. And then we iterate
        through all the positions and speeds, and we calculate the time as target - p / s
        and then we create a stack and add this value. Then the key is compare recent
        with second most recent stack contingent on both being available and most recent is less than
        or equal to second most recent then pop. After iterating through stack contains all that either
        merge or form their own fleet
        """

        # tuple array
        pair = [(p, s) for p, s in zip(position, speed)]

        # reverse in decreasing
        pair.sort(reverse=True)

        # iterate and add to stack and pop
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)