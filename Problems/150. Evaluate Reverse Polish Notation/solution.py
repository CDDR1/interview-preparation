import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(l - r)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l / r))
            else: 
                stack.append(int(token))
                
        return stack[-1]
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Stack
# Time used: 24min before watching video solution