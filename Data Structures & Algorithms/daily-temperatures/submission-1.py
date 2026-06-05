class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # start out everything 0
        # stack to basically log every day, and if we encounter a day which resolves then change result if not leave it
        result = [0] * len(temperatures)
        stack = [] # (temp, index)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = index - stack_index
            stack.append((temp, index))
        return result