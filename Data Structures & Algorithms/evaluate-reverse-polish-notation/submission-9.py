class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                res = stack[-1] + stack[-2]
                stack.pop()
                stack[-1] = res

            elif tokens[i] == "*":
                res = stack[-1] * stack[-2]
                stack.pop()
                stack[-1] = res
                
            
            elif tokens[i] == "-":
                res = stack[-2] - stack[-1]
                stack.pop()
                stack[-1] = res

            elif tokens[i] == "/":
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack[-1] = res

            else:
                stack.append(int(tokens[i]))

        return stack[-1]