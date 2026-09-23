class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(int(i))
            elif (len(stack) >= 2):
                if i == '+':
                    stack[-2] += stack[-1]
                elif i == '-':
                    stack[-2] -= stack[-1]
                elif i == '*':
                    stack[-2] *= stack[-1]
                else:
                    stack[-2] = int(stack[-2]/stack[-1])
                stack.pop()
    
        return stack[0]
