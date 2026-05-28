class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # loop through once make a result array
        # return result array summed
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operations[i]))

        return sum(stack)