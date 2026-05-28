class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # loop through once make a result array
        # return result array summed
        stack = []
        res = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "C":
                res -= stack.pop()
            elif operations[i] == "D":
                res += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operations[i]))
                res += int(operations[i])

        return res