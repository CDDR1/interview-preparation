class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []
        includesClosing = False
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                pair = stack.pop() + c
                includesClosing = True
                if pair != '()' and pair != '[]' and pair != '{}':
                    return False
                
        if len(stack) != 0:
            return False
                
        return includesClosing
        
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Stack
# Time used: 24min
        