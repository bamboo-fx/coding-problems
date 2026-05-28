class Solution:
    def isValid(self, s: str) -> bool:
        # dictionary of closing and corresponding opening brackets
        # iterate through s, keep a stack of open parentheses
        # anytime we see closed and stack contains open version, remove it
        # if stack is empty true else false

        dic = { ")": "(", "]": "[", "}": "{"}
        stack = []
        for i in range(len(s)):
            if s[i] not in dic:
                stack.append(s[i])
            elif s[i] in dic:
                if stack and dic[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        return False if stack else True